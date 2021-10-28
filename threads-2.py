import threading

threadObj = threading.Thread(target = print, args = ["Hello", "How"],
                             kwargs = {'sep': ' aba nicht so '})
threadObj.start()
