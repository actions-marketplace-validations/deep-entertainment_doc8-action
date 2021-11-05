from doc8 import doc8
import os

try:
    result = doc8(
        paths=os.environ.get("INPUT_SCANPATHS").split(','),
        ignore_path=os.environ.get("INPUT_IGNOREPATHS").split(',')
    )

    print("::set-output name=files_selected::%d" % result.files_selected)
    print("::set-output name=files_ignored::%d" % result.files_ignored)
    print("::set-output name=total_errors::%d" % result.total_errors)

    if os.environ.get("INPUT_ADDANNOTATIONS") == 'true':
        for error in result.errors:
            print("::error file=%s,line=%d,endLine=%d,title=%s::%s" % (
                error[1],
                error[2],
                error[2],
                error[3],
                error[4]
            ))

    print(result.report())

    if result.total_errors > 0:
        exit(1)

except UnicodeDecodeError as error:
    print("A document contains invalid unicode characters. We can't find the specific document, though: %s" % error)
