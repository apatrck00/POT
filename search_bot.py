import re
import datetime
from time import time

pattern_find_email = r'[\w\.-]+@[\w\.-]+'  # pattern for emails in html code
pattern_find_links = r'http[s]?://[^\s<>"]+|www.[^\s<>"]+'  # pattern fpr links in html code
pattern_find_images_jpg = r'src="https://.*.jpg)"'

strainer_email_de = '.de'
strainer_email_at = '.at'
strainer_email_com = '.com'
strainer_email_eu = '.eu'

strainer_email_sum_german = [strainer_email_de, strainer_email_at, strainer_email_com, strainer_email_eu]

# Var global for general use of other method's
actual_global_link = ''


def strainer(var_list, strainer_list):
    tuple_var = tuple(strainer_list)
    list_new = [x for x in var_list if x.endswith(tuple_var)]
    return list_new


# Var for patterns which is used in the function 'get_all_pattern_from_site'
var_modify_pattern = []


def get_all_pattern_from_site(var_text_var):
    global var_modify_pattern
    pattern_res_var = []
    for loop_pattern in var_modify_pattern:
        pattern_res_var += re.findall(loop_pattern, var_text_var)
    return pattern_res_var


# returns all the html code from a site
def get_all_from_site(var_url):
    import urllib.request
    site = urllib.request.urlopen(var_url)
    return str(site.read())


# Search in html code for verbs
var_modify_search = ['Patrick', 'Prader']
var_result_verbs = []


def is_verb_in_txt(text_var):
    global var_modify_search
    global var_result_verbs
    global actual_global_link

    var_result_verbs = []

    for i in var_modify_search:
        if not text_var.find(i) == -1:
            var_result_verbs.append([actual_global_link, i, text_var.count(i)])
            return 1
    return -1


# returns a list of email addresses which was found in 'text_var'
def get_emails_from_txt(text_var):
    global pattern_find_email
    email_var = re.findall(pattern_find_email, text_var)
    return email_var


# returns a list of all links which was found in 'text_var'
def get_links_from_txt(text_var):
    global pattern_find_links
    links = re.findall(pattern_find_links, text_var)
    return links


def crawl_for(max_websites, timeout_seconds, max_count, starter_url=r'https://stackoverflow.com',
              function_var=[get_emails_from_txt], var_strainer=False,
              do_output=False, do_output_links=False, do_timestamp=False):
    results = []
    linky_list = [starter_url]
    web_searched_count = 0
    stamp_future = time() + timeout_seconds
    shown_do_output = 0

    global actual_global_link

    while web_searched_count < max_websites and time() < stamp_future and len(linky_list) > web_searched_count:
        if max_count < len(results):
            return results
        if do_output_links and len(linky_list) > 0:
            ttt = ''
            if do_timestamp:
                ttt = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S   ')
            print(ttt + '[-]      ' + linky_list[web_searched_count])
        try:
            act_txt = get_all_from_site(linky_list[web_searched_count])
            actual_global_link = linky_list[web_searched_count]
        except KeyboardInterrupt:
            raise KeyboardInterrupt
        except:
            web_searched_count += 1
            continue
        linky_list = linky_list + get_links_from_txt(act_txt)
        linky_list = sorted(set(linky_list), key=linky_list.index)

        for loop_function in function_var:
            short_res = loop_function(act_txt)
            if short_res == 1:
                results.append(linky_list[web_searched_count])
            elif short_res == -1:
                pass
            else:
                results += short_res

        results = sorted(set(results), key=results.index)
        if var_strainer:
            results = strainer(results, var_strainer)

        if do_output and len(results) > 0:
            while shown_do_output < len(results):
                ttt = ''
                if do_timestamp:
                    ttt = datetime.datetime.fromtimestamp(time()).strftime('%Y-%m-%d %H:%M:%S   ')
                print(ttt + '   [+]      ' + results[shown_do_output])

                if var_result_verbs:
                    for out_extra in var_result_verbs:
                        if out_extra[2] > 0:
                            print(ttt + "      [x]      '" + out_extra[1] + "' found:   " + str(out_extra[2]))

                shown_do_output += 1

        web_searched_count += 1

    return results


