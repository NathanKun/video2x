#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Waifu2x NCNN Vulkan x Anime4k Driver
Author: NathanKun
Date Created: Sept 09, 2019

Dev: NathanKun
"""

# local imports
from anime4k import Anime4k
from waifu2x_ncnn_vulkan import Waifu2xNcnnVulkan

# built-in imports
import threading


class Waifu2xNcnnVulkanXAnime4k:
    """This class wraps Waifu2xNcnnVulkan class and Anume4k class

    An object will be created for this class, containing information
    about the binary address and the processing method. When being called
    by the main program, other detailed information will be passed to
    the upscale function.
    """

    def __init__(self, waifu2x_settings):
        self.waifu2x_settings = waifu2x_settings
        self.print_lock = threading.Lock()

    def upscale(self, input_directory, output_directory, scale_ratio, upscaler_exceptions):
        """This is the core function for Waifu2xNcnnVulkanXAnime4k class

        Arguments:
            input_directory {string} -- source directory path
            output_directory {string} -- output directory path
            ratio {int} -- output video ratio
        """
        w2_output_dir = output_directory + "Tmp"
        
        w2_vulkan = Waifu2xNcnnVulkan(copy.deepcopy(self.waifu2x_settings))
        w2_return = w2_vulkan.upscale(input_directory, w2_output_dir, scale_ratio, upscaler_exceptions);
        
        if len(upscaler_exceptions) != 0:
            return "Waifu2xNcnnVulkan return: \n" + str(w2_return) + "\n\n Waifu2xNcnnVulkan throws exception"
        
        anime4k = Anime4k(copy.deepcopy(self.waifu2x_settings))
        anime4k_return = anime4k.upscale(w2_output_dir, output_directory, scale_ratio, upscaler_exceptions);

        return "Waifu2xNcnnVulkan return: \n" + str(w2_return) + "\n\nAnime4k return: \n" + str(anime4k_return)


