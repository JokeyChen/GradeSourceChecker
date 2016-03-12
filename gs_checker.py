def main():
    url = raw_input('Please specify the GradeSource website you want to check:')
    if len(url) == 0:
        print 'Empty url. Program aborts.'
        return
    try:
        interval = int(raw_input('Please specify the checking interval (in minute):'))
    except ValueError:
        print 'Invalid interval. Program aborts.'
        return

if __name__ == '__main__':
    main()