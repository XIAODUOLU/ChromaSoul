#!/usr/bin/env python
# -*- coding: utf-8 -*-

from color_transfer.libs import TransferFactory
from color_transfer.utils import ImageUtils


def main():
    # init image transfer
    transfer = TransferFactory.create("mean_std")

    # load the images
    img_ref = ImageUtils.load_img("color_transfer/test_img/reference.jpg")
    img = ImageUtils.load_img("color_transfer/test_img/input.jpg")

    # load the images
    transfer.extract(img_ref)
    img_tgt = transfer.transfer(img)

    ImageUtils.save_img(img_tgt, "color_transfer/output/target.jpg")


if __name__ == "__main__":
    main()
