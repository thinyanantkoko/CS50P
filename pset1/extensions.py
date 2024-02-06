def main():
    #prompting the user for filename to check its media type by extension
    f_name = input("File name: ")
    #ignoring any leading/trailing whitespaces and the case
    f_name = f_name.strip().casefold()

    match f_name:
        case f_name if f_name.endswith(".gif"):
            print("image/gif")
        case f_name if f_name.endswith((".jpg", ".jpeg")):
            print("image/jpeg")
        case f_name if f_name.endswith(".png"):
            print("image/png")
        case f_name if f_name.endswith(".pdf"):
            print("application/pdf")
        case f_name if f_name.endswith(".txt"):
            print("text/plain")
        case f_name if f_name.endswith(".zip"):
            print("application/zip")
        case _:
            #for extensions excluded in mentioned ones or no extension at all
            print("application/octet-stream")

main()