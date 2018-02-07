import sys
import time
import search_bot

banner = "" \
            "\r\n" \
            " .----------------.  .----------------.  .----------------. \r\n" \
            "| .--------------. || .--------------. || .--------------. |\r\n" \
            "| |   ______     | || |     ____     | || |  _________   | |\r\n" \
            "| |  |_   __ \\   | || |   .'    `.   | || | |  _   _  |  | |\r\n" \
            "| |    | |__) |  | || |  /  .--.  \\  | || | |_/ | | \\_|  | |\r\n" \
            "| |    |  ___/   | || |  | |    | |  | || |     | |      | |\r\n"  \
            "| |   _| |_      | || |  \\  `--'  /  | || |    _| |_     | |\r\n"  \
            "| |  |_____|     | || |   `.____.'   | || |   |_____|    | |\r\n"  \
            "| |              | || |              | || |              | |\r\n"  \
           "| '--------------' || '--------------' || '--------------' |\r\n"  \
            " '----------------'  '----------------'  '----------------' \r\n" \
            "by Patrick Prader\r\n\r\n\r\n"

usage = 'Usage:\r\n\r\n' \
        '-d   ||   -date           Do output for time [default=False]\r\n' \
        "-h   ||   -help           Shows this help-menu\r\n" \
        '-l   ||   -links          Show link from actual site searching on [default=False]\r\n' \
        '-o   ||   -output         Do output for results [default=True]\r\n' \
        "-pp  ||   -PP             Show some information's about the developer\r\n" \
        "-r   ||   -results        Count of maximal results before [default=60^60]\r\n" \
        "-s   ||   -search         Search for ['links','emails','verbs verb_one,verb_two'] [default='emails']\r\n" \
        '-st  ||   -strainer       Filter the results by end. Example: -st .at,.eu [default=none]\r\n' \
        '-t   ||   -timeout        Time in seconds of duration from searching [default=60^60]\r\n' \
        '-u   ||   -url            Start url [default=https:\\\\github.com]\r\n' \
        '-w   ||   -websites       Count of maximal searched websites [default=60^60]\r\n\r\n\r\n' \

my_info = "This tool was written by me in the age of 16 years.\r\n" \
          "I think the tool is useful and can help you some\r\n" \
          "some times by information gathering or finding emails\r\n" \
          "from your darling.\r\n" \
          "I know there are a lot of options to improve an I will\r\n" \
          "go after it. But this takes much time, so I have publicised,\r\n" \
          "it, so please do not feel disturbed by some bugs or other \r\n" \
          "random stuff like this\r\n" \
          "If you find bugs you can contact me ono pradersplit12@gmail.com\r\n" \
          "You also can send me some new ideas for this tool\r\n" \
          "Fell free to contact me!!\r\n" \

unknown_command = 'Unknown command\r\n' \
                  'Please check your syntax and try again'
unknown_search_command = 'Unknown command'
file_error = 'ERROR_FILE - Results can not be saved'
finish = 'SUCCESS'

# Main
if __name__ == "__main__":
    try:
        print(banner)
        if len(sys.argv) == 1:
            print(usage)
            sys.exit(0)

        #var_search_for = ''
        var_url = ''
        var_timeout = 60*10
        var_do_output = True
        var_do_output_links = False
        var_write_to_file = -1
        var_max_count_websites = 60**60
        var_max_results = 60**60
        var_strainer = False
        var_do_output_timestamp = False
        var_function = []

        i = 0
        while len(sys.argv) > i+1:
            i += 1
            sys_argv_i_var = sys.argv[i]
            if sys_argv_i_var == '-s' or sys_argv_i_var == '-search':
                i += 1
                sys_argv_i_var = sys.argv[i]
                #var_search_for = []
                loc_var = sys_argv_i_var.split(',')

                for loc_argument in loc_var:

                    if loc_argument == 'emails':
                        var_function.append(search_bot.get_emails_from_txt)
                    elif loc_argument == 'links':
                        var_function.append(search_bot.get_links_from_txt)
                    elif loc_argument == 'verbs':
                        var_function.append(search_bot.is_verb_in_txt)
                        i += 1
                        sys_argv_i_var = sys.argv[i]
                        search_bot.var_modify_search = sys_argv_i_var.split(',')


                continue
            elif sys_argv_i_var == '-u' or sys.argv[i] == '-url':
                i += 1
                var_url = sys.argv[i]
                continue
            elif sys_argv_i_var == '-t' or sys_argv_i_var == '-timeout':
                i += 1
                var_timeout = int(sys.argv[i])
                continue
            elif sys_argv_i_var == '-o' or sys_argv_i_var == '-output':
                i += 1
                var_do_output = bool(sys.argv[i])
                continue
            elif sys_argv_i_var == '-f' or sys_argv_i_var == '-file':
                i += 1
                var_write_to_file = sys.argv[i]
                continue
            elif sys_argv_i_var == '-w' or sys_argv_i_var == '-websites':
                i += 1
                var_max_count_websites = int(sys.argv[i])
                continue
            elif sys_argv_i_var == '-r' or sys_argv_i_var == '-results':
                i += 1
                var_max_results = int(sys.argv[i])
                continue
            elif sys_argv_i_var == '-l' or sys_argv_i_var == '-links':
                i += 1
                var_do_output_links = bool(sys.argv[i])
                continue
            elif sys_argv_i_var == '-st' or sys_argv_i_var == '-strainer':
                i += 1
                var_strainer = sys.argv[i].split(',')
                continue
            elif sys_argv_i_var == '-d' or sys_argv_i_var == '-date':
                i += 1
                var_do_output_timestamp = bool(sys.argv[i])
                continue
            elif sys_argv_i_var == '-h' or sys_argv_i_var == '-help':
                print(usage)
                sys.exit(0)
            elif sys_argv_i_var == '-pp' or sys_argv_i_var == '-PP':
                print(my_info)
                sys.exit(0)
            else:
                print(unknown_command)
                sys.exit(0)

        var_time_stamp = time.time()
        res = search_bot.crawl_for(var_max_count_websites, var_timeout, var_max_results, var_url,
                                   var_function, var_strainer, var_do_output, var_do_output_links, var_do_output_timestamp)
        if not var_write_to_file == -1:
            try:
                f = open(var_write_to_file, 'w')
                for line in res:
                    f.write(line)
                    f.write('\n')
                f.flush()
                f.close()
                print('Results has been saved to :   ' + var_write_to_file)
            except:
                print(file_error)

        print('Remaining [seconds]:   ' + str(int((time.time() - var_time_stamp))))
        print('Found              :   ' + str(len(res)))
        print(finish)

    except KeyboardInterrupt:
        print('INTERRUPTED')
        sys.exit(0)
 #   except:
  #      print('\r\n\r\n'
   #           'INTERNAL-ERROR')
    #    print('An internal ERROR has occurred')
     #   print('Pleas contact the developer to fix this error')
      #  sys.exit(1)

