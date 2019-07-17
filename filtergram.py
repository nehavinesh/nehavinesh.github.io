import filter

def main():
    new_image = filter.load_img("table.JPG")
    obama_pic = filter.obamicon(new_image)
    filter.show_img(obama_pic)
    #filter.show_img(new_image)

if __name__ == "__main__":
    main()
