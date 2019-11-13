import numpy as np


"""Abell 76"""
abell76imagename = 'abell76_wfpc2_pc.fits'
abell76centre = 477, 518    # Centre y, x (don't ask)
abell76offset = 2.7, -0.5   # Pixel offset off of centre x, y +ve moves to the right and up
abell76size = 120
abell76angle = np.pi/2
abell76eccentricity = 0.1
abell76ir = [10.778, 10.861, 10.529, 8.446]
# Nuker Law Initial Guess
abell76ci = 6
abell76br = 6
abell76g = -0.02
abell76t = 1.50764
abell76b = 1.5199
abell76params = abell76ci, abell76br, abell76g, abell76t, abell76b
# Any Image coreections: rotate 90, image ellipse correction
abell76rot = 'no', 0.9
abell76gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell76 = abell76centre, abell76size, abell76angle, abell76eccentricity,\
          abell76params, abell76offset, abell76gs, abell76rot, 60, 33.37, abell76ir


"""Abell 119"""
abell119imagename = 'abell119_wfpc2_pc.fits'
abell119centre = 464, 435    # Centre y, x (don't ask)
abell119offset = 12.1, -6.1   # Pixel offset off of centre x, y +ve moves to the right and up
abell119size = 100
abell119angle = np.pi/2 - 0.38
abell119eccentricity = 0.45
abell119ir = [11.284, 11.371, 10.906, 8.082]
# Nuker Law Initial Guess
abell119ci = 0.9
abell119br = 25
abell119g = -0.00200167
abell119t = 2.250764
abell119b = 1.76199
abell119params = abell119ci, abell119br, abell119g, abell119t, abell119b
# Any Image coreections: rotate 90, image ellipse correction
abell119rot = 'no', 0.9
abell119gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell119 = abell119centre, abell119size, abell119angle, abell119eccentricity,\
           abell119params, abell119offset, abell119gs, abell119rot, 80, 155.68, abell119ir


"""Abell 147"""
abell147imagename = 'abell147_wfpc2_pc.fits'
abell147centre = 518, 417    # Centre y, x (don't ask)
# abell147offset = 2.7, -3.5   # Pixel offset off of centre x, y +ve moves to the right and up
abell147offset = 0.1, -0.1   # Pixel offset off of centre x, y +ve moves to the right and up
abell147size = 100
abell147angle = np.pi/2 + 0.51
abell147eccentricity = 0.6
abell147ir = [11.143, 11.176, 10.552, 8.081]
# Nuker Law Initial Guess
abell147ci = 9
abell147br = 6.48
abell147g = -0.186
abell147t = 1.430764
abell147b = 1.724
abell147params = abell147ci, abell147br, abell147g, abell147t, abell147b
# Any Image coreections: rotate 90, image ellipse correction
abell147rot = 'yes', 0.9
abell147gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell147 = abell147centre, abell147size, abell147angle, abell147eccentricity,\
           abell147params, abell147offset, abell147gs, abell147rot, 80, 151.63, abell147ir


"""Abell 160"""
abell160imagename = 'abell160_wfpc2_f814w.fits'
abell160centre = 1112, 625    # Centre y, x (don't ask)
abell160offset = 4.5, -1.3   # Pixel offset off of centre x, y +ve moves to the right and up
abell160size = 50
abell160iterations = 50
abell160angle = np.pi
abell160eccentricity = 0.1
abell160ir = [11.684, 11.731, 10.947, 9.021]
# Nuker Law Initial Guess
abell160ci = 2.3905
abell160br = 10.476
abell160g = -0.0843
abell160t = 4.01738
abell160b = 1.14201
abell160params = abell160ci, abell160br, abell160g, abell160t, abell160b
# Any Image coreections: rotate 90, image ellipse correction
abell160rot = 'no', 0.9
abell160gs = 3
"""Final List: holding all the BCGs individual parameters:::::"""
abell160 = abell160centre, abell160size, abell160angle, abell160eccentricity, \
           abell160params, abell160offset, abell160gs, abell160rot, abell160iterations, 153.53, abell160ir


"""Abell 168"""
abell168imagename = 'abell168_wfpc2_pc.fits'
abell168centre = 445, 498    # Centre y, x (don't ask)
abell168offset = 1.5, -1.0   # Pixel offset off of centre x, y +ve moves to the right and up
abell168size = 100
abell168angle = np.pi/2 - 0.3
abell168eccentricity = 0.4
abell168ir = [11.321, 11.388, 10.824, 8.352]
# Nuker Law Initial Guess
abell168ci = 37.51
abell168br = 2.53
abell168g = 0.00600167
abell168t = 1.50764
abell168b = 1.5199
abell168params = abell168ci, abell168br, abell168g, abell168t, abell168b
# Any Image coreections: rotate 90, image ellipse correction
abell168rot = 'yes', 0.9
abell168gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell168 = abell168centre, abell168size, abell168angle, abell168eccentricity,\
           abell168params, abell168offset, abell168gs, abell168rot, 130, 155.68, abell168ir


"""Abell 189"""
abell189imagename = 'abell189_wfpc2_pc.fits'
abell189centre = 414, 503    # Centre y, x (don't ask)
abell189offset = 2.5, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
abell189size = 100
abell189angle = np.pi/2
abell189eccentricity = 0.64
abell189ir = [11.238, 11.289, 10.202, 8.416]
# Nuker Law Initial Guess
abell189ci = 6.2
abell189br = 6.91
abell189g = -0.030600167
abell189t = 1.3450764
abell189b = 1.622199
abell189params = abell189ci, abell189br, abell189g, abell189t, abell189b
# Any Image coreections: rotate 90, image ellipse correction
abell189rot = 'yes', 0.75
abell189gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell189 = abell189centre, abell189size, abell189angle, abell189eccentricity,\
           abell189params, abell189offset, abell189gs, abell189rot, 100,  116.71, abell189ir


"""Abell 193"""
abell193imagename = 'abell193_wfpc2_pc.fits'
abell193centre = 403, 581    # Centre y, x (don't ask)
abell193offset = 0.2, 0.6   # Pixel offset off of centre x, y +ve moves to the right and up
abell193size = 24
abell193angle = np.pi/2 + 0.45
abell193eccentricity = 0.6
abell193ir = [10.854, 10.875, 10.371, 8.362]
# Nuker Law Initial Guess
abell193ci = 6
abell193br = 6
abell193g = 0.0600167
abell193t = 1.50764
abell193b = 1.5199
abell193params = abell193ci, abell193br, abell193g, abell193t, abell193b
# Any Image coreections: rotate 90, image ellipse correction
abell193rot = 'no', 0.9
abell193gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell193 = abell193centre, abell193size, abell193angle, abell193eccentricity,\
           abell193params, abell193offset, abell193gs, abell193rot, 24, 167.98, abell193ir


"""Abell 195"""
abell195imagename = 'Abell195_08683_09_wfpc2_f814w_pc_drz.fits'
abell195centre = 515, 528    # Centre y, x (don't ask)
abell195offset = 0.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
abell195size = 100
abell195angle = np.pi/2
abell195eccentricity = 0.43
abell195ir = [11.288, 11.273, 10.50, 8.593]
# Nuker Law Initial Guess
abell195ci = 37.51
abell195br = 2.53
abell195g = 0.00600167
abell195t = 1.50764
abell195b = 1.5199
abell195params = abell195ci, abell195br, abell195g, abell195t, abell195b
# Any Image coreections: rotate 90, image ellipse correction
abell195rot = 'no', 0.9
abell195gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell195 = abell195centre, abell195size, abell195angle, abell195eccentricity,\
           abell195params, abell195offset, abell195gs, abell195rot, 100, 150.16, abell195ir


"""Abell 260"""
a260imagename = 'Abell260_08683_10_wfpc2_f814w_pc_drz.fits'
a260centre = 440, 393    # Centre y, x (don't ask)
a260offset = -7.2, 2.6   # Pixel offset off of centre x, y +ve moves to the right and up
a260size = 125
a260angle = np.pi/2 + np.pi/4
a260eccentricity = 0.5
a260ir = [10.807, 10.875, 10.27, 8.517]
# Nuker Law Initial Guess
a260ci = 37.51
a260br = 2.53
a260g = 0.00600167
a260t = 1.50764
a260b = 1.5199
a260params = a260ci, a260br, a260g, a260t, a260b
# Any Image coreections: rotate 90, image ellipse correction
a260rot = 'yes', 0.9
a260gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell260 = a260centre, a260size, a260angle, a260eccentricity, \
           a260params, a260offset, a260gs, a260rot, 130, 131.58, a260ir


# """Abell 261"""
# a261imagename = 'Abell261_08683_11_wfpc2_f814w_pc_drz.fits'
# a261centre = 564, 542    # Centre y, x (don't ask)
# a261offset = 1.8, -3.5   # Pixel offset off of centre x, y +ve moves to the right and up
# a261size = 80
# a261angle = np.pi/2 + 0.23
# a261eccentricity = 0.77
# a261ir = [11.395, 11.429, 10.749, 8.893]
# # Nuker Law Initial Guess
# a261ci = 6
# a261br = 6
# a261g = 0.0600167
# a261t = 1.50764
# a261b = 1.5199
# a261params = a261ci, a261br, a261g, a261t, a261b
# # Any Image coreections: rotate 90, image ellipse correction
# a261rot = 'yes', 0.8
# a261gs = 5
# """Final List: holding all the BCGs individual parameters:::::"""
# abell261 = a261centre, a261size, a261angle, a261eccentricity, \
#            a261params, a261offset, a261gs, a261rot, 70, 158.89, a261ir


"""Abell 262"""
a262imagename = 'Abell262_10884_05_wfpc2_f622w_pc_drz.fits'
a262centre = 496, 521    # Centre y, x (don't ask)
a262offset = 3.2, -1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a262size = 100
a262angle = 0.93
a262eccentricity = 0.3
a262ir = [10.427, 10.522, 9.434, 8.397]
# Nuker Law Initial Guess
a262ci = 2
a262br = 10
a262g = -0.0800167
a262t = 4.50764
a262b = 1.8199
a262params = a262ci, a262br, a262g, a262t, a262b
# Any Image coreections: rotate 90, image ellipse correction
a262rot = 'no', 0.9
a262gs = 8
"""Final List: holding all the BCGs individual parameters:::::"""
abell262 = a262centre, a262size, a262angle, a262eccentricity, \
           a262params, a262offset, a262gs, a262rot, 105, 62.63, a262ir


"""Abell 295"""
a295imagename = 'Abell295_08683_13_wfpc2_f814w_pc_drz.fits'
a295centre = 554, 438    # Centre y, x (don't ask)
a295offset = +0.2, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a295size = 100
a295angle = np.pi/2 - 0.4
a295eccentricity = 0.33
a295ir = [11.305, 11.355, 10.802, 8.826]
# Nuker Law Initial Guess
a295ci = 2.5
a295br = 19.55
a295g = -0.00700167
a295t = 1.6347
a295b = 2.0314
a295params = a295ci, a295br, a295g, a295t, a295b
# Any Image coreections: rotate 90, image ellipse correction
a295rot = 'no', 0.9
a295gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell295 = a295centre, a295size, a295angle, a295eccentricity, \
           a295params, a295offset, a295gs, a295rot, 100, 147.10, a295ir


"""Abell 347"""
a347imagename = 'Abell347_08683_14_wfpc2_f814w_pc_drz.fits'
a347centre = 384, 391    # Centre y, x (don't ask)
a347offset = -4.2, 3.5   # Pixel offset off of centre x, y +ve moves to the right and up
a347size = 70
a347angle = np.pi/2 - 0.8
a347eccentricity = 0.8
a347ir = [11.01, 11.04, 10.597, 8.383]
# Nuker Law Initial Guess
a347ci = 4.5
a347br = 5.53
a347g = -0.00900167
a347t = 2.970764
a347b = 0.965199
a347params = a347ci, a347br, a347g, a347t, a347b
# Any Image coreections: rotate 90, image ellipse correction
a347rot = 'no', 0.9
a347gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell347 = a347centre, a347size, a347angle, a347eccentricity, \
           a347params, a347offset, a347gs, a347rot, 70, 70.95, a347ir


"""Abell 376"""
a376imagename = 'Abell376_15_wfpc2_f814w_pc_drz.fits'
a376centre = 508, 521    # Centre y, x (don't ask)
a376offset = 0.1, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a376size = 100
a376angle = np.pi/2 + 0.1
a376eccentricity = 0.45
a376ir = [11.513, 11.559, 11.003, 9.027]
# Nuker Law Initial Guess
a376ci = 4.5
a376br = 5.53
a376g = -0.00900167
a376t = 2.970764
a376b = 0.965199
a376params = a376ci, a376br, a376g, a376t, a376b
# Any Image coreections: rotate 90, image ellipse correction
a376rot = 'no', 0.9
a376gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell376 = a376centre, a376size, a376angle, a376eccentricity, \
           a376params, a376offset, a376gs, a376rot, 70, 70.95, a376ir


"""Abell 397"""
a397imagename = 'Abell397_08683_16_wfpc2_f814w_pc_drz.fits'
a397centre = 613, 554    # Centre y, x (don't ask)
a397offset = +5.2, -5.1   # Pixel offset off of centre x, y +ve moves to the right and up
a397size = 100
a397angle = np.pi/2 + 0.6
a397eccentricity = 0.6
a397ir = [10.911, 10.942, 10.444, 8.24]
# Nuker Law Initial Guess
a397ci = 1.9
a397br = 22.9
a397g = 0.00765
a397t = 2.090764
a397b = 2.0095
a397params = a397ci, a397br, a397g, a397t, a397b
# Any Image coreections: rotate 90, image ellipse correction
a397rot = 'yes', 0.9
a397gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell397 = a397centre, a397size, a397angle, a397eccentricity, \
           a397params, a397offset, a397gs, a397rot, 100, 116.34, a397ir


"""Abell 419"""
a419imagename = 'Abell419_08683_18_wfpc2_f814w_pc_drz.fits'
a419centre = 423, 514    # Centre y, x (don't ask)
a419offset = +0.5, -0.9   # Pixel offset off of centre x, y +ve moves to the right and up
a419size = 50
a419angle = np.pi/2 - 0.5
a419eccentricity = 0.63
a419ir = [11.747, 11.826, 10.98, 8.836]
# Nuker Law Initial Guess
a419ci = 37.51
a419br = 2.53
a419g = 0.00600167
a419t = 1.50764
a419b = 1.5199
a419params = a419ci, a419br, a419g, a419t, a419b
# Any Image coreections: rotate 90, image ellipse correction
a419rot = 'yes', 0.9
a419gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell419 = a419centre, a419size, a419angle, a419eccentricity, \
           a419params, a419offset, a419gs, a419rot, 50, 136.49, a419ir


"""Abell 496"""
a496imagename = 'Abell496_08683_19_wfpc2_f814w_pc_drz.fits'
a496centre = 550, 547    # Centre y, x (don't ask)
a496offset = +1.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a496size = 100
a496angle = np.pi/2 - 0.39
a496eccentricity = 0.55
a496ir = [10.996, 11.026, 10.361, 8.942]
# Nuker Law Initial Guess
a496ci = 1.7
a496br = 27.1
a496g = 0.00487600167
a496t = 1.170764
a496b = 1.89199
a496params = a496ci, a496br, a496g, a496t, a496b
# Any Image coreections: rotate 90, image ellipse correction
a496rot = 'yes', 0.9
a496gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell496 = a496centre, a496size, a496angle, a496eccentricity, \
           a496params, a496offset, a496gs, a496rot, 100, 110.97, a496ir


"""Abell 533"""
a533imagename = 'Abell533_08683_20_wfpc2_f814w_pc_drz.fits'
a533centre = 528, 420    # Centre y, x (don't ask)
a533offset = +0.2, -1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a533size = 100
a533angle = np.pi/2 + 0.42
a533eccentricity = 0.51
a533ir = [11.507, 11.528, 11.03, 8.81]
# Nuker Law Initial Guess
a533ci = 4.737
a533br = 7.7658
a533g = -0.0230167
a533t = 1.4784
a533b = 1.63599
a533params = a533ci, a533br, a533g, a533t, a533b
# Any Image coreections: rotate 90, image ellipse correction
a533rot = 'no', 0.9
a533gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell533 = a533centre, a533size, a533angle, a533eccentricity, \
           a533params, a533offset, a533gs, a533rot, 100, 156.97, a533ir


"""Abell 548"""
a548imagename = 'Abell548_08683_22_wfpc2_f814w_pc_drz.fits'
a548centre = 408, 368    # Centre y, x (don't ask)
a548offset = 1.2, -0.5   # Pixel offset off of centre x, y +ve moves to the right and up
a548size = 100
a548angle = np.pi/2 - 0.45
a548eccentricity = 0.72
a548ir = [11.392, 11.378, 10.667, 8.652]
# Nuker Law Initial Guess
a548ci = 4.7371
a548br = 7.675
a548g = -0.02369
a548t = 1.4764
a548b = 1.6359
a548params = a548ci, a548br, a548g, a548t, a548b
# Any Image coreections: rotate 90, image ellipse correction
a548rot = 'no', 0.9
a548gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell548 = a548centre, a548size, a548angle, a548eccentricity, \
           a548params, a548offset, a548gs, a548rot, 100, 133.52, a548ir


# """Abell 569"""
# a569imagename = 'Abell569_06673_12_wfpc2_f814w_f555w_pc_sci.fits'
# a569centre = 1195, 716    # Centre y, x (don't ask)
# a569offset = -1.5, 0.5   # Pixel offset off of centre x, y +ve moves to the right and up
# a569size = 80
# a569angle = np.pi/2 + 0.1
# a569eccentricity = 0.58
# a569ir = [10.213, 10.207, 9.177, 7.816]
# # Nuker Law Initial Guess
# a569ci = 5.51
# a569br = 5.53
# a569g = -0.0600167
# a569t = 11.50764
# a569b = 1.5199
# a569params = a569ci, a569br, a569g, a569t, a569b
# # Any Image coreections: rotate 90, image ellipse correction
# a569rot = 'yes', 0.9
# a569gs = 5
# """Final List: holding all the BCGs individual parameters:::::"""
# abell569 = a569centre, a569size, a569angle, a569eccentricity, \
#            a569params, a569offset, a569gs, a569rot, 80, 73.32, a569ir


"Abell 634"
a634imagename = 'Abell634_08683_25_wfpc2_f814w_pc_drz.fits'
a634centre = 385, 431    # Centre y, x (don't ask)
a634offset = -1.8, 0.7   # Pixel offset off of centre x, y +ve moves to the right and up
a634size = 120
a634angle = np.pi/2 + 0.35
a634eccentricity = 0.55
a634ir = [10.899, 10.943, 10.33, 8.889]
# Nuker Law Initial Guess
a634ci = 3.3751
a634br = 7.522
a634g = 0.00290167
a634t = 1.91764
a634b = 1.5199
a634params = a634ci, a634br, a634g, a634t, a634b
# Any Image coreections: rotate 90, image ellipse correction
a634rot = 'no', 0.9
a634gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell634 = a634centre, a634size, a634angle, a634eccentricity, \
           a634params, a634offset, a634gs, a634rot, 100, 102.62, a634ir


"Abell 671"
a671imagename = 'Abell671_08683_26_wfpc2_f814w_pc_drz.fits'
a671centre = 423, 436    # Centre y, x (don't ask)
a671offset = +0.2, -15.1   # Pixel offset off of centre x, y +ve moves to the right and up
a671size = 100
a671angle = np.pi/2 + 0.5
a671eccentricity = 0.6
a671ir = [11.079, 11.123, 10.313, 8.845]
# Nuker Law Initial Guess
a671ci = 37.51
a671br = 2.53
a671g = 0.00600167
a671t = 1.50764
a671b = 1.5199
a671params = a671ci, a671br, a671g, a671t, a671b
# Any Image coreections: rotate 90, image ellipse correction
a671rot = 'yes', 0.9
a671gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell671 = a671centre, a671size, a671angle, a671eccentricity, \
           a671params, a671offset, a671gs, a671rot, 100, 176.68, a671ir


"Abell 779"
a779imagename = 'Abell779_08683_27_wfpc2_f814w_pc_drz.fits'
a779centre = 465, 277    # Centre y, x (don't ask)
a779offset = 2.1, 3.3   # Pixel offset off of centre x, y +ve moves to the right and up
a779size = 100
a779angle = np.pi/2 - 0.77
a779eccentricity = 0.5
a779ir = [9.91, 9.932, 9.464, 8.243]
# Nuker Law Initial Guess
a779ci = 37.51
a779br = 2.53
a779g = 0.00600167
a779t = 1.50764
a779b = 1.5199
a779params = a779ci, a779br, a779g, a779t, a779b
# Any Image coreections: rotate 90, image ellipse correction
a779rot = 'yes', 0.9
a779gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell779 = a779centre, a779size, a779angle, a779eccentricity, \
           a779params, a779offset, a779gs, a779rot, 100, 84.66, a779ir


"Abell 912"
a912imagename = 'Abell912_08683_28_wfpc2_f814w_pc_drz.fits'
a912centre = 564, 491    # Centre y, x (don't ask)
a912offset = 0.2, -0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a912size = 70
a912angle = np.pi/2 - 0.55
a912eccentricity = 0.58
a912ir = [11.84, 11.894, 10.894, 8.74]
# Nuker Law Initial Guess
a912ci = 37.51
a912br = 2.53
a912g = 0.00600167
a912t = 1.50764
a912b = 1.5199
a912params = a912ci, a912br, a912g, a912t, a912b
# Any Image coreections: rotate 90, image ellipse correction
a912rot = 'no', 0.9
a912gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell912 = a912centre, a912size, a912angle, a912eccentricity, \
           a912params, a912offset, a912gs, a912rot, 70, 153.96, a912ir


"Abell 999"
a999imagename = 'Abell999_08683_30_wfpc2_f814w_pc_drz.fits'
a999centre = 523, 530    # Centre y, x (don't ask)
a999offset = 1.2, -1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a999size = 100
a999angle = np.pi/2 - 0.18
a999eccentricity = 0.55
a999ir = [10.927, 10.983, 10.443, 8.631]
# Nuker Law Initial Guess
a999ci = 37.51
a999br = 2.53
a999g = 0.00600167
a999t = 1.50764
a999b = 1.5199
a999params = a999ci, a999br, a999g, a999t, a999b
# Any Image coreections: rotate 90, image ellipse correction
a999rot = 'yes', 0.9
a999gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell999 = a999centre, a999size, a999angle, a999eccentricity, \
           a999params, a999offset, a999gs, a999rot, 130, 112.82, a999ir


"Abell 1016"
a1016imagename = 'Abell1016_08683_31_wfpc2_f814w_pc_drz.fits'
a1016centre = 529, 532    # Centre y, x (don't ask)
a1016offset = 2.5, -2.7   # Pixel offset off of centre x, y +ve moves to the right and up
a1016size = 100
a1016angle = np.pi/2 + 0.3
a1016eccentricity = 0.58
a1016ir = [11.113, 11.205, 10.511, 8.511]
# Nuker Law Initial Guess
a1016ci = 37.51
a1016br = 2.53
a1016g = 0.00600167
a1016t = 1.50764
a1016b = 1.5199
a1016params = a1016ci, a1016br, a1016g, a1016t, a1016b
# Any Image coreections: rotate 90, image ellipse correction
a1016rot = 'yes', 0.9
a1016gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1016 = a1016centre, a1016size, a1016angle, a1016eccentricity, \
           a1016params, a1016offset, a1016gs, a1016rot, 100, 112.81, a1016ir


# The Defn of Centre changes here:
"Abell 1060"
a1060imagename = 'Abell1060_06554_03_wfpc2_f814w_pc_drz.fits'
a1060centre = 462, 552    # Centre y, x (don't ask)
a1060offset = 0.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1060size = 100
a1060angle = 0.3
a1060eccentricity = 0.4
a1060ir = [10.439, 10.48, 9.283, 7.488]
# Nuker Law Initial Guess
a1060ci = 0.9
a1060br = 40
a1060g = -0.0799500167
a1060t = 1.00150764
a1060b = 1.080199
a1060params = a1060ci, a1060br, a1060g, a1060t, a1060b
# Any Image coreections: rotate 90, image ellipse correction
a1060rot = 'no', 0.8
a1060gs = 8
"""Final List: holding all the BCGs individual parameters:::::"""
abell1060 = a1060centre, a1060size, a1060angle, a1060eccentricity, \
           a1060params, a1060offset, a1060gs, a1060rot, 100, 38.63, a1060ir


"Abell 1142"
a1142imagename = 'Abell1142_08683_35_wfpc2_f814w_pc_drz.fits'
a1142centre = 459, 419    # Centre y, x (don't ask)
a1142offset = -0.4, 2.5   # Pixel offset off of centre x, y +ve moves to the right and up
a1142size = 100
a1142angle = np.pi/2 + 0.48
a1142eccentricity = 0.65
a1142ir = [11.082, 11.117, 10.534, 8.218]
# Nuker Law Initial Guess
a1142ci = 11.51
a1142br = 3.53
a1142g = 0.010600167
a1142t = 2.350764
a1142b = 1.38199
a1142params = a1142ci, a1142br, a1142g, a1142t, a1142b
# Any Image coreections: rotate 90, image ellipse correction
a1142rot = 'yes', 0.9
a1142gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1142 = a1142centre, a1142size, a1142angle, a1142eccentricity, \
           a1142params, a1142offset, a1142gs, a1142rot, 70, 121.48, a1142ir


"Abell 1177"
a1177imagename = 'Abell1177_08683_36_wfpc2_f814w_pc_drz.fits'
a1177centre = 406, 364    # Centre y, x (don't ask)
a1177offset = +0.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1177size = 100
a1177angle = np.pi/2 - 0.8
a1177eccentricity = 0.58
a1177ir = [10.992, 11.074, 10.309, 8.568]
# Nuker Law Initial Guess
a1177ci = 37.51
a1177br = 2.53
a1177g = 0.00600167
a1177t = 1.50764
a1177b = 1.5199
a1177params = a1177ci, a1177br, a1177g, a1177t, a1177b
# Any Image coreections: rotate 90, image ellipse correction
a1177rot = 'no', 0.9
a1177gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1177 = a1177centre, a1177size, a1177angle, a1177eccentricity, \
           a1177params, a1177offset, a1177gs, a1177rot, 100, 113.81, a1177ir


"Abell 1228"
a1228imagename = 'Abell1228_08683_39_wfpc2_f814w_pc_drz.fits'
a1228centre = 430, 400    # Centre y, x (don't ask)
a1228offset = -0.10005, -0.3   # Pixel offset off of centre x, y +ve moves to the right and up
a1228size = 100
a1228angle = np.pi/2 + 0.42
a1228eccentricity = 0.5
a1228ir = [11.265, 11.33, 10.622, 8.75]
# Nuker Law Initial Guess
a1228ci = 37.51
a1228br = 2.53
a1228g = 0.00600167
a1228t = 1.50764
a1228b = 1.5199
a1228params = a1228ci, a1228br, a1228g, a1228t, a1228b
# Any Image coreections: rotate 90, image ellipse correction
a1228rot = 'yes', 0.9
a1228gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1228 = a1228centre, a1228size, a1228angle, a1228eccentricity, \
           a1228params, a1228offset, a1228gs, a1228rot, 80, 133.56, a1228ir


"Abell 1308"
a1308imagename = 'Abell1308_08683_42_wfpc2_f814w_pc_drz.fits'
a1308centre = 536, 476    # Centre y, x (don't ask)
a1308offset = -0.5, 0.8   # Pixel offset off of centre x, y +ve moves to the right and up
a1308size = 100
a1308angle = np.pi/2 - 0.45
a1308eccentricity = 0.43
a1308ir = [11.25, 11.246, 9.936, 7.953]
# Nuker Law Initial Guess
a1308ci = 4.96
a1308br = 6.08
a1308g = 0.0992800167
a1308t = 2.41
a1308b = 1.485599
a1308params = a1308ci, a1308br, a1308g, a1308t, a1308b
# Any Image coreections: rotate 90, image ellipse correction
a1308rot = 'yes', 0.9
a1308gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1308 = a1308centre, a1308size, a1308angle, a1308eccentricity, \
           a1308params, a1308offset, a1308gs, a1308rot, 100, 172.42, a1308ir


"Abell 1314"
a1314imagename = 'Abell1314_08683_43_wfpc2_f814w_pc_drz.fits'
a1314centre = 528, 476    # Centre y, x (don't ask)
a1314offset = -1.2, -0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1314size = 100
a1314angle = np.pi/2 - 0.1
a1314eccentricity = 0.7
a1314ir = [10.772, 10.82, 10.177, 8.508]
# Nuker Law Initial Guess
a1314ci = 3.8
a1314br = 58.53
a1314g = -0.011600167
a1314t = 1.040764
a1314b = 3.855199
a1314params = a1314ci, a1314br, a1314g, a1314t, a1314b
# Any Image coreections: rotate 90, image ellipse correction
a1314rot = 'no', 0.9
a1314gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1314 = a1314centre, a1314size, a1314angle, a1314eccentricity, \
           a1314params, a1314offset, a1314gs, a1314rot, 100, 123.14, a1314ir


"Abell 1367"
a1367imagename = 'Abell1367_06587_05_wfpc2_f555w_pc_drz.fits'
a1367centre = 501, 498    # Centre y, x (don't ask)
a1367offset = -1.2, -0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1367size = 100
a1367angle = np.pi/2
a1367eccentricity = 0.4
a1367ir = [10.244, 10.27, 9.821, 8.226]
# Nuker Law Initial Guess
a1367ci = 37.51
a1367br = 2.53
a1367g = 0.00600167
a1367t = 1.50764
a1367b = 1.5199
a1367params = a1367ci, a1367br, a1367g, a1367t, a1367b
# Any Image coreections: rotate 90, image ellipse correction
a1367rot = 'yes', 0.9
a1367gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1367 = a1367centre, a1367size, a1367angle, a1367eccentricity, \
           a1367params, a1367offset, a1367gs, a1367rot, 100, 77.58, a1367ir


"Abell 1631"
a1631imagename = 'Abell1631_08683_45_wfpc2_f814w_pc_drz.fits'
a1631centre = 437, 481    # Centre y, x (don't ask)
a1631offset = +0.4, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1631size = 100
a1631angle = np.pi/2 - 0.6
a1631eccentricity = 0.58
a1631ir = [11.321, 11.337, 10.908, 8.957]
# Nuker Law Initial Guess
a1631ci = 9.1
a1631br = 5.453
a1631g = -0.109167
a1631t = 1.20764
a1631b = 1.6199
a1631params = a1631ci, a1631br, a1631g, a1631t, a1631b
# Any Image coreections: rotate 90, image ellipse correction
a1631rot = 'yes', 0.9
a1631gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1631 = a1631centre, a1631size, a1631angle, a1631eccentricity, \
           a1631params, a1631offset, a1631gs, a1631rot, 100, 154.63, a1631ir


"Abell 1656"
a1656imagename = 'Abell1656_08200_01_wfpc2_f606w_pc_drz.fits'
a1656centre = 386, 385    # Centre y, x (don't ask)
a1656offset = 0.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1656size = 100
a1656angle = np.pi/2 - 0.05
a1656eccentricity = 0.7
a1656ir = [9.827, 9.882, 9.384, 8.297]
# Nuker Law Initial Guess
a1656ci = 3.51
a1656br = 48.53
a1656g = 0.03600167
a1656t = 1.80764
a1656b = 2.5199
a1656params = a1656ci, a1656br, a1656g, a1656t, a1656b
# Any Image coreections: rotate 90, image ellipse correction
a1656rot = 'no', 0.9
a1656gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1656 = a1656centre, a1656size, a1656angle, a1656eccentricity, \
           a1656params, a1656offset, a1656gs, a1656rot, 80, 83.06, a1656ir


"Abell 1795"
a1795imagename = 'Abell1795_04_wfpc2_f555w_pc_drz.fits'
a1795centre = 438, 549    # Centre y, x (don't ask)
a1795offset = 0.1, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1795size = 100
a1795angle = np.pi/2
a1795eccentricity = 0.43
a1795ir = [11.995, 11.997, 10.582, 8.891]
# Nuker Law Initial Guess
a1795ci = 3.51
a1795br = 48.53
a1795g = 0.03600167
a1795t = 1.80764
a1795b = 2.5199
a1795params = a1795ci, a1795br, a1795g, a1795t, a1795b
# Any Image coreections: rotate 90, image ellipse correction
a1795rot = 'yes', 0.9
a1795gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1795 = a1795centre, a1795size, a1795angle, a1795eccentricity, \
           a1795params, a1795offset, a1795gs, a1795rot, 80, 83.06, a1795ir


"Abell 1836"
a1836imagename = 'Abell1836_08683_49_wfpc2_f814w_pc_drz.fits'
a1836centre = 508, 483    # Centre y, x (don't ask)
a1836offset = -0.7, 0.5   # Pixel offset off of centre x, y +ve moves to the right and up
a1836size = 100
a1836angle = np.pi/2 + 0.3
a1836eccentricity = 0.2
a1836ir = [10.832, 10.904, 10.159, 8.368]
# Nuker Law Initial Guess
a1836ci = 37.51
a1836br = 2.53
a1836g = 0.00600167
a1836t = 1.50764
a1836b = 1.5199
a1836params = a1836ci, a1836br, a1836g, a1836t, a1836b
# Any Image coreections: rotate 90, image ellipse correction
a1836rot = 'yes', 0.9
a1836gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1836 = a1836centre, a1836size, a1836angle, a1836eccentricity, \
           a1836params, a1836offset, a1836gs, a1836rot, 100, 122.33, a1836ir


"Abell 1983"
a1983imagename = 'abell1983_08683_50_wfpc2_f814w_pc_drz.fits'
a1983centre = 467, 488    # Centre y, x (don't ask)
a1983offset = -1.7, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a1983size = 125
a1983angle = np.pi/2 + 0.5
a1983eccentricity = 0.7
a1983ir = [11.23, 11.346, 10.494, 8.729]
# Nuker Law Initial Guess
a1983ci = 37.51
a1983br = 2.53
a1983g = 0.00600167
a1983t = 1.50764
a1983b = 1.5199
a1983params = a1983ci, a1983br, a1983g, a1983t, a1983b
# Any Image coreections: rotate 90, image ellipse correction
a1983rot = 'yes', 0.9
a1983gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell1983 = a1983centre, a1983size, a1983angle, a1983eccentricity, \
           a1983params, a1983offset, a1983gs, a1983rot, 130, 154.07, a1983ir


"Abell 2040"
a2040imagename = 'images/abell2040'
a2040centre = 431, 438    # Centre y, x (don't ask)
a2040offset = 0.2, -0.6   # Pixel offset off of centre x, y +ve moves to the right and up
a2040size = 125
a2040angle = np.pi/2 + 0.6
a2040eccentricity = 0.33
a2040ir = [11.745, 11.815, 11.097, 9.49]
# Nuker Law Initial Guess
a2040ci = 37.51
a2040br = 2.53
a2040g = 0.00600167
a2040t = 1.50764
a2040b = 1.5199
a2040params = a2040ci, a2040br, a2040g, a2040t, a2040b
# Any Image coreections: rotate 90, image ellipse correction
a2040rot = 'no', 0.9
a2040gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2040 = a2040centre, a2040size, a2040angle, a2040eccentricity, \
           a2040params, a2040offset, a2040gs, a2040rot, 130, 154.46, a2040ir, a2040imagename


"Abell 2052"
a2052imagename = 'Abell2052_08683_52_wfpc2_f814w_pc_drz.fits'
a2052centre = 405, 469    # Centre y, x (don't ask)
a2052offset = 0.2, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2052size = 100
a2052angle = np.pi/2 + 0.6
a2052eccentricity = 0.5
a2052ir = [11.376, 11.423, 10.378, 8.197]
# Nuker Law Initial Guess
a2052ci = 2.11
a2052br = 2.63
a2052g = -0.08800167
a2052t = 2.50764
a2052b = 0.769199
a2052params = a2052ci, a2052br, a2052g, a2052t, a2052b
# Any Image coreections: rotate 90, image ellipse correction
a2052rot = 'yes', 0.8
a2052gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2052 = a2052centre, a2052size, a2052angle, a2052eccentricity, \
           a2052params, a2052offset, a2052gs, a2052rot, 50, 120.21, a2052ir


"Abell 2147"
a2147imagename = 'Abell2147_08683_55_wfpc2_f814w_pc_drz.fits'
a2147centre = 403, 383    # Centre y, x (don't ask)
a2147offset = -1.1, 1.6   # Pixel offset off of centre x, y +ve moves to the right and up
a2147size = 100
a2147angle = np.pi/2 + 0.2
a2147eccentricity = 0.58
a2147ir = [11.289, 11.365, 10.709, 9.02]
# Nuker Law Initial Guess
a2147ci = 37.51
a2147br = 2.53
a2147g = 0.00600167
a2147t = 1.50764
a2147b = 1.5199
a2147params = a2147ci, a2147br, a2147g, a2147t, a2147b
# Any Image coreections: rotate 90, image ellipse correction
a2147rot = 'yes', 0.9
a2147gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2147 = a2147centre, a2147size, a2147angle, a2147eccentricity, \
           a2147params, a2147offset, a2147gs, a2147rot, 100, 122.47, a2147ir


"Abell 2162"
a2162imagename = 'Abell2162_07281_40_wfpc2_f814w_pc_drz.fits'
a2162centre = 453, 602    # Centre y, x (don't ask)
a2162offset = +0.2, 2.7   # Pixel offset off of centre x, y +ve moves to the right and up
a2162size = 100
a2162angle = np.pi/2 + 0.15
a2162eccentricity = 0.57
a2162ir = [10.610, 10.661, 10.15, 8.939]
# Nuker Law Initial Guess
a2162ci = 37.51
a2162br = 2.53
a2162g = 0.00600167
a2162t = 1.50764
a2162b = 1.5199
a2162params = a2162ci, a2162br, a2162g, a2162t, a2162b
# Any Image coreections: rotate 90, image ellipse correction
a2162rot = 'yes', 0.9
a2162gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2162 = a2162centre, a2162size, a2162angle, a2162eccentricity, \
           a2162params, a2162offset, a2162gs, a2162rot, 100, 114.82, a2162ir


"""Abell 2197"""
abell2197imagename = 'abell2197_wfpc2_f814w.fits'
abell2197centre = 1000, 620    # Centre y, x (don't ask)
abell2197offset = -1.1, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
abell2197size = 120
abell2197angle = np.pi/4
abell2197eccentricity = 0.7
abell2197ir = [10.257, 10.293, 9.783, 8.26]
# Nuker Law Initial Guess
abell2197ci = 56
abell2197br = 6.15
abell2197g = -0.219
abell2197t = 0.83477
abell2197b = 1.751
abell2197params = abell2197ci, abell2197br, abell2197g, abell2197t, abell2197b
# Any Image coreections: rotate 90, image ellipse correction
abell2197rot = 'yes', 0.76
abell2197gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2197 = abell2197centre, abell2197size, abell2197angle, abell2197eccentricity,\
            abell2197params, abell2197offset, abell2197gs, abell2197rot, 100, 110.4, abell2197ir


"Abell 2247"
a2247imagename = 'Abell2247_08683_61_wfpc2_f814w_pc_drz.fits'
a2247centre = 338, 343    # Centre y, x (don't ask)
a2247offset = -0.9, -0.6   # Pixel offset off of centre x, y +ve moves to the right and up
a2247size = 100
a2247angle = np.pi/2 + 0.1
a2247eccentricity = 0.5
a2247ir = [11.247, 11.284, 9.902, 8.631]
# Nuker Law Initial Guess
a2247ci = 2.51
a2247br = 5.53
a2247g = -0.04600167
a2247t = 1.50764
a2247b = 1.5199
a2247params = a2247ci, a2247br, a2247g, a2247t, a2247b
# Any Image coreections: rotate 90, image ellipse correction
a2247rot = 'yes', 0.9
a2247gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2247 = a2247centre, a2247size, a2247angle, a2247eccentricity, \
           a2247params, a2247offset, a2247gs, a2247rot, 70, 142.86, a2247ir


"Abell 2572"
a2572imagename = 'Abell2572_08683_62_wfpc2_f814w_pc_drz.fits'
a2572centre = 400, 589    # Centre y, x (don't ask)
a2572offset = 0.6, -1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2572size = 100
a2572angle = np.pi/2 + 0.22
a2572eccentricity = 0.58
a2572ir = [10.848, 10.952, 10.842, 8.861]
# Nuker Law Initial Guess
a2572ci = 14.51
a2572br = 4.53
a2572g = -0.017600167
a2572t = 1.00764
a2572b = 1.6199
a2572params = a2572ci, a2572br, a2572g, a2572t, a2572b
# Any Image coreections: rotate 90, image ellipse correction
a2572rot = 'no', 0.9
a2572gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2572 = a2572centre, a2572size, a2572angle, a2572eccentricity, \
           a2572params, a2572offset, a2572gs, a2572rot, 100, 150.47, a2572ir


"Abell 2589"
a2589imagename = 'Abell2589_08683_63_wfpc2_f814w_pc_drz.fits'
a2589centre = 451, 507    # Centre y, x (don't ask)
a2589offset = -0.5, 0.6   # Pixel offset off of centre x, y +ve moves to the right and up
a2589size = 100
a2589angle = np.pi/2 - 0.11
a2589eccentricity = 0.53
a2589ir = [11.239, 11.315, 10.65, 8.487]
# Nuker Law Initial Guess
a2589ci = 3.51
a2589br = 7.253
a2589g = -0.0600167
a2589t = 1.720764
a2589b = 1.42199
a2589params = a2589ci, a2589br, a2589g, a2589t, a2589b
# Any Image coreections: rotate 90, image ellipse correction
a2589rot = 'yes', 0.9
a2589gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2589 = a2589centre, a2589size, a2589angle, a2589eccentricity, \
           a2589params, a2589offset, a2589gs, a2589rot, 100, 150.03, a2589ir


"Abell 2593"
a2593imagename = 'Abell2593_08683_64_wfpc2_f814w_pc_drz.fits'
a2593centre = 619, 470    # Centre y, x (don't ask)
a2593offset = -1.2, -1.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2593size = 100
a2593angle = np.pi/2 - 0.18
a2593eccentricity = 0.2
a2593ir = [11.469, 11.513, 10.627, 8.636]
# Nuker Law Initial Guess
a2593ci = 37.51
a2593br = 2.53
a2593g = 0.00600167
a2593t = 1.50764
a2593b = 1.5199
a2593params = a2589ci, a2589br, a2589g, a2589t, a2589b
# Any Image coreections: rotate 90, image ellipse correction
a2593rot = 'no', 0.9
a2593gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2593 = a2593centre, a2593size, a2593angle, a2593eccentricity, \
           a2593params, a2593offset, a2593gs, a2593rot, 100, 150.75, a2593ir


"Abell 2634"
a2634imagename = 'Abell2634_08683_65_wfpc2_f814w_pc_drz.fits'
a2634centre = 406, 528    # Centre y, x (don't ask)
a2634offset = 0.1, -0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2634size = 100
a2634angle = np.pi/2 + 0.3
a2634eccentricity = 0.4
a2634ir = [10.359, 10.409, 9.603, 7.935]
# Nuker Law Initial Guess
a2634ci = 37.51
a2634br = 2.53
a2634g = 0.00600167
a2634t = 1.50764
a2634b = 1.5199
a2634params = a2634ci, a2634br, a2634g, a2634t, a2634b
# Any Image coreections: rotate 90, image ellipse correction
a2634rot = 'yes', 0.9
a2634gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2634 = a2634centre, a2634size, a2634angle, a2634eccentricity, \
           a2634params, a2634offset, a2634gs, a2634rot, 100, 113.97, a2634ir


"Abell 2657"
a2657imagename = 'Abell2657_08683_66_wfpc2_f814w_pc_drz.fits'
a2657centre = 507, 472    # Centre y, x (don't ask)
a2657offset = 0.5, 0.5   # Pixel offset off of centre x, y +ve moves to the right and up
a2657size = 80
a2657angle = np.pi/2 - 0.12
a2657eccentricity = 0.6
a2657ir = [11.433, 11.445, 9.486, 7.412]
# Nuker Law Initial Guess
a2657ci = 2.51
a2657br = 2.53
a2657g = 0.11600167
a2657t = 8.50764
a2657b = 0.9199
a2657params = a2657ci, a2657br, a2657g, a2657t, a2657b
# Any Image coreections: rotate 90, image ellipse correction
a2657rot = 'no', 0.9
a2657gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2657 = a2657centre, a2657size, a2657angle, a2657eccentricity, \
           a2657params, a2657offset, a2657gs, a2657rot, 100, 146.25, a2657ir


"Abell 2666"
a2666imagename = 'Abell2666_08683_67_wfpc2_f814w_pc_drz.fits'
a2666centre = 436, 316    # Centre y, x (don't ask)
a2666offset = -0.6, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2666size = 100
a2666angle = np.pi/2 - 0.56
a2666eccentricity = 0.6
a2666ir = [10.347, 10.379, 9.808, 8.376]
# Nuker Law Initial Guess
a2666ci = 37.51
a2666br = 2.53
a2666g = 0.00600167
a2666t = 1.50764
a2666b = 1.5199
a2666params = a2666ci, a2666br, a2666g, a2666t, a2666b
# Any Image coreections: rotate 90, image ellipse correction
a2666rot = 'no', 0.9
a2666gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2666 = a2666centre, a2666size, a2666angle, a2666eccentricity, \
           a2666params, a2666offset, a2666gs, a2666rot, 100, 101.23, a2666ir


"Abell 2877"
a2877imagename = 'Abell2877_08683_72_wfpc2_f814w_pc_drz.fits'
a2877centre = 486, 513    # Centre y, x (don't ask)
a2877offset = -0.5, 0.1   # Pixel offset off of centre x, y +ve moves to the right and up
a2877size = 100
a2877angle = np.pi/2 + 0.59
a2877eccentricity = 0.4
a2877ir = [9.623, 9.649, 9.113, 7.821]
# Nuker Law Initial Guess
a2877ci = 7.51
a2877br = 20.53
a2877g = 0.00600167
a2877t = 1.50764
a2877b = 1.8199
a2877params = a2877ci, a2877br, a2877g, a2877t, a2877b
# Any Image coreections: rotate 90, image ellipse correction
a2877rot = 'no', 0.9
a2877gs = 5
"""Final List: holding all the BCGs individual parameters:::::"""
abell2877 = a2877centre, a2877size, a2877angle, a2877eccentricity, \
           a2877params, a2877offset, a2877gs, a2877rot, 100, 86.10, a2877ir


"""Abell 3144"""
abell3144imagename = 'abell3144_wfpc2_total.fits'
abell3144centre = 538, 440       # Centre y, x (don't ask)
abell3144offset = 0.5, -0.3      # Pixel offset off of centre x, y +ve moves to the right and up
abell3144size = 125
abell3144iterations = 150
abell3144angle = np.pi / 2 + 0.23
abell3144eccentricity = 0.64
abell3144ir = [11.443, 11.427, 10.927, 9.348]
# Nuker Law Initial Guess
abell3144ci = 6.174
abell3144br = 7.3189
abell3144g = -0.01351
abell3144t = 1.596
abell3144b = 1.8808
abell3144params = abell3144ci, abell3144br, abell3144g, abell3144t, abell3144b
# Any Image coreections: rotate 90, image ellipse correction
abell3144rot = 'no', 0.75
abell3144gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3144 = abell3144centre, abell3144size, abell3144angle, abell3144eccentricity, \
            abell3144params, abell3144offset, abell3144gs, abell3144rot, abell3144iterations, 320.4, abell3144ir


"""Abell 3193"""
a3193imagename = 'Abell3193_08683_77_wfpc2_f814w_pc_drz.fits'
a3193centre = 565, 471       # Centre y, x (don't ask)
a3193offset = -0.7, -1.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3193size = 100
a3193iterations = 100
a3193angle = np.pi / 2 + 0.15
a3193eccentricity = 0.45
a3193ir = [10.975, 11.034, 10.439, 9.584]
# Nuker Law Initial Guess
a3193ci = 6.174
a3193br = 7.3189
a3193g = -0.01351
a3193t = 1.596
a3193b = 1.8808
a3193params = a3193ci, a3193br, a3193g, a3193t, a3193b
# Any Image coreections: rotate 90, image ellipse correction
a3193rot = 'no', 0.8
a3193gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3193 = a3193centre, a3193size, a3193angle, a3193eccentricity, \
            a3193params, a3193offset, a3193gs, a3193rot, a3193iterations, 115.88, a3193ir


"""Abell 3376"""
a3376imagename = 'Abell3376_08683_80_wfpc2_f814w_pc_drz.fits'
a3376centre = 587, 493       # Centre y, x (don't ask)
a3376offset = 0.5, -0.3      # Pixel offset off of centre x, y +ve moves to the right and up
a3376size = 100
a3376iterations = 100
a3376angle = np.pi / 2 - 0.4
a3376eccentricity = 0.64
a3376ir = [11.339, 11.333, 10.777, 8.766]
# Nuker Law Initial Guess
a3376ci = 6.174
a3376br = 7.3189
a3376g = -0.01351
a3376t = 1.596
a3376b = 1.8808
a3376params = a3376ci, a3376br, a3376g, a3376t, a3376b
# Any Image coreections: rotate 90, image ellipse correction
a3376rot = 'no', 0.75
a3376gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3376 = a3376centre, a3376size, a3376angle, a3376eccentricity, \
            a3376params, a3376offset, a3376gs, a3376rot, a3376iterations, 154.03, a3376ir


"""Abell 3395"""
a3395imagename = 'Abell3395_08683_83_wfpc2_f814w_pc_drz.fits'
a3395centre = 326, 362       # Centre y, x (don't ask)
a3395offset = 0.4, -0.4      # Pixel offset off of centre x, y +ve moves to the right and up
a3395size = 100
a3395iterations = 100
a3395angle = np.pi / 2 + 0.58
a3395eccentricity = 0.64
a3395ir = [11.68, 11.718, 11.04, 9.0047]
# Nuker Law Initial Guess
a3395ci = 6.174
a3395br = 7.3189
a3395g = -0.01351
a3395t = 1.596
a3395b = 1.8808
a3395params = a3395ci, a3395br, a3395g, a3395t, a3395b
# Any Image coreections: rotate 90, image ellipse correction
a3395rot = 'no', 0.75
a3395gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3395 = a3395centre, a3395size, a3395angle, a3395eccentricity, \
            a3395params, a3395offset, a3395gs, a3395rot, a3395iterations, 162.85, a3395ir


"""Abell 3526"""
a3526imagename = 'Abell3526_05956_01_wfpc2_f702w_pc_drz.fits'
a3526centre = 1549, 1101       # Centre y, x (don't ask)
a3526offset = 0.1, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3526size = 100
a3526iterations = 100
a3526angle = np.pi/2 + 0.5
a3526eccentricity = 0.45
a3526ir = [9.663, 9.653, 8.947, 7.573]
# Nuker Law Initial Guess
a3526ci = 13.174
a3526br = 16.3189
a3526g = -0.03351
a3526t = 1.596
a3526b = 1.5808
a3526params = a3526ci, a3526br, a3526g, a3526t, a3526b
# Any Image coreections: rotate 90, image ellipse correction
a3526rot = 'no', 0.9
a3526gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3526 = a3526centre, a3526size, a3526angle, a3526eccentricity, \
            a3526params, a3526offset, a3526gs, a3526rot, a3526iterations, 35.04, a3526ir


"""Abell 3528"""
a3528imagename = 'Abell3528_08683_85_wfpc2_f814w_pc_drz.fits'
a3528centre = 1509, 1151       # Centre y, x (don't ask)
a3528offset = -0.1, 1.6      # Pixel offset off of centre x, y +ve moves to the right and up
a3528size = 80
a3528iterations = 60
a3528angle = np.pi / 2 - 0.03
a3528eccentricity = 0.58
a3528ir = [11.172, 11.199, 10.609, 9.156]
# Nuker Law Initial Guess
a3528ci = 6.174
a3528br = 7.3189
a3528g = -0.01351
a3528t = 1.596
a3528b = 1.8808
a3528params = a3528ci, a3528br, a3528g, a3528t, a3528b
# Any Image coreections: rotate 90, image ellipse correction
a3528rot = 'yes', 0.9
a3528gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3528 = a3528centre, a3528size, a3528angle, a3528eccentricity, \
            a3528params, a3528offset, a3528gs, a3528rot, a3528iterations, 178.98, a3528ir


"""Abell 3532"""
a3532imagename = 'Abell3532_08683_87_wfpc2_f814w_pc_drz.fits'
a3532centre = 506, 414       # Centre y, x (don't ask)
a3532offset = 0.1, 0.5      # Pixel offset off of centre x, y +ve moves to the right and up
a3532size = 100
a3532iterations = 80
a3532angle = np.pi / 2 + 0.75
a3532eccentricity = 0.58
a3532ir = [11.607, 11.603, 10.978, 8.676]
# Nuker Law Initial Guess
a3532ci = 2.174
a3532br = 7.3189
a3532g = 0.0441351
a3532t = 2.596
a3532b = 1.4808
a3532params = a3532ci, a3532br, a3532g, a3532t, a3532b
# Any Image coreections: rotate 90, image ellipse correction
a3532rot = 'yes', 0.75
a3532gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3532 = a3532centre, a3532size, a3532angle, a3532eccentricity, \
            a3532params, a3532offset, a3532gs, a3532rot, a3532iterations, 182.47, a3532ir


"""Abell 3554"""
a3554imagename = 'Abell3554_08683_91_wfpc2_f814w_pc_drz.fits'
a3554centre = 484, 454       # Centre y, x (don't ask)
a3554offset = -0.3, -5.7      # Pixel offset off of centre x, y +ve moves to the right and up
a3554size = 80
a3554iterations = 60
a3554angle = np.pi / 2 + 0.1
a3554eccentricity = 0.48
a3554ir = [11.768, 11.796, 11.317, 8.845]
# Nuker Law Initial Guess
a3554ci = 1.22174
a3554br = 13.3189
a3554g = -0.01351
a3554t = 1.596
a3554b = 1.8808
a3554params = a3554ci, a3554br, a3554g, a3554t, a3554b
# Any Image coreections: rotate 90, image ellipse correction
a3554rot = 'no', 0.75
a3554gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3554 = a3554centre, a3554size, a3554angle, a3554eccentricity, \
            a3554params, a3554offset, a3554gs, a3554rot, a3554iterations, 158.29, a3554ir


"""Abell 3556"""
a3556imagename = 'Abell3556_92_wfpc2_f814w_pc_drz.fits'
a3556centre = 581, 526       # Centre y, x (don't ask)
a3556offset = -0.8, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3556size = 80
a3556iterations = 60
a3556angle = np.pi / 2 - 0.6
a3556eccentricity = 0.77
a3556ir = [10.965, 11.039, 10.468, 8.878]
# Nuker Law Initial Guess
a3556ci = 4.1
a3556br = 7.3189
a3556g = -0.01351
a3556t = 1.596
a3556b = 1.8808
a3556params = a3556ci, a3556br, a3556g, a3556t, a3556b
# Any Image coreections: rotate 90, image ellipse correction
a3556rot = 'yes', 0.9
a3556gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3556 = a3556centre, a3556size, a3556angle, a3556eccentricity, \
            a3556params, a3556offset, a3556gs, a3556rot, a3556iterations, 160.12, a3556ir


"""Abell 3558"""
a3558imagename = 'Abell3558_08683_93_wfpc2_f814w_pc_drz.fits'
a3558centre = 452, 406       # Centre y, x (don't ask)
a3558offset = 0.2, 0.2      # Pixel offset off of centre x, y +ve moves to the right and up
a3558size = 80
a3558iterations = 80
a3558angle = np.pi / 2 - 0.25
a3558eccentricity = 0.4
a3558ir = [11.176, 11.233, 10.709, 9.152]
# Nuker Law Initial Guess
a3558ci = 6.174
a3558br = 7.3189
a3558g = 0.01351
a3558t = 1.596
a3558b = 1.8808
a3558params = a3558ci, a3558br, a3558g, a3558t, a3558b
# Any Image coreections: rotate 90, image ellipse correction
a3558rot = 'yes', 0.9
a3558gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3558 = a3558centre, a3558size, a3558angle, a3558eccentricity, \
            a3558params, a3558offset, a3558gs, a3558rot, a3558iterations, 158.29, a3558ir


"""Abell 3559"""
a3559imagename = 'Abell3559_08683_94_wfpc2_f814w_pc_drz.fits'
a3559centre = 435, 575       # Centre y, x (don't ask)
a3559offset = -0.5, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3559size = 100
a3559iterations = 100
a3559angle = np.pi / 2 - 0.27
a3559eccentricity = 0.68
a3559ir = [11.003, 11.005, 10.374, 8.478]
# Nuker Law Initial Guess
a3559ci = 6.174
a3559br = 7.3189
a3559g = -0.01351
a3559t = 1.596
a3559b = 1.8808
a3559params = a3559ci, a3559br, a3559g, a3559t, a3559b
# Any Image coreections: rotate 90, image ellipse correction
a3559rot = 'no', 0.75
a3559gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3559 = a3559centre, a3559size, a3559angle, a3559eccentricity, \
            a3559params, a3559offset, a3559gs, a3559rot, a3559iterations, 157.12, a3559ir


"""Abell 3562"""
a3562imagename = 'Abell3562_08683_96_wfpc2_f814w_pc_drz.fits'
a3562centre = 498, 600       # Centre y, x (don't ask)
a3562offset = -0.5, -0.2      # Pixel offset off of centre x, y +ve moves to the right and up
a3562size = 100
a3562iterations = 100
a3562angle = np.pi / 2 + 0.2
a3562eccentricity = 0.48
a3562ir = [11.525, 11.604, 11.026, 8.835]
# Nuker Law Initial Guess
a3562ci = 6.174
a3562br = 7.3189
a3562g = -0.01351
a3562t = 1.596
a3562b = 1.8808
a3562params = a3562ci, a3562br, a3562g, a3562t, a3562b
# Any Image coreections: rotate 90, image ellipse correction
a3562rot = 'no', 0.9
a3562gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3562 = a3562centre, a3562size, a3562angle, a3562eccentricity, \
            a3562params, a3562offset, a3562gs, a3562rot, a3562iterations, 162.37, a3562ir


"""Abell 3564"""
a3564imagename = 'Abell3564_08683_97_wfpc2_f814w_pc_drz.fits'
a3564centre = 452, 569       # Centre y, x (don't ask)
a3564offset = 0.3, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3564size = 80
a3564iterations = 80
a3564angle = np.pi / 2 + 0.04
a3564eccentricity = 0.58
a3564ir = [11.587, 11.65, 10.846, 8.655]
# Nuker Law Initial Guess
a3564ci = 6.174
a3564br = 7.3189
a3564g = -0.01351
a3564t = 1.596
a3564b = 1.8808
a3564params = a3564ci, a3564br, a3564g, a3564t, a3564b
# Any Image coreections: rotate 90, image ellipse correction
a3564rot = 'yes', 0.9
a3564gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3564 = a3564centre, a3564size, a3564angle, a3564eccentricity, \
            a3564params, a3564offset, a3564gs, a3564rot, a3564iterations, 167.90, a3564ir


"""Abell 3565"""
a3565imagename = 'Abell3563_05910_03_wfpc2_f814w_pc_drz.fits'
a3565centre = 513, 551       # Centre y, x (don't ask)
a3565offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3565size = 100
a3565iterations = 80
a3565angle = np.pi / 2 - 0.2
a3565eccentricity = 0.43
a3565ir = [8.969, 8.993, 8.315, 6.624]
# Nuker Law Initial Guess
a3565ci = 10.174
a3565br = 10.3189
a3565g = 0.01351
a3565t = 1.596
a3565b = 1.8808
a3565params = a3565ci, a3565br, a3565g, a3565t, a3565b
# Any Image coreections: rotate 90, image ellipse correction
a3565rot = 'no', 0.9
a3565gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3565 = a3565centre, a3565size, a3565angle, a3565eccentricity, \
            a3565params, a3565offset, a3565gs, a3565rot, a3565iterations, 39.72, a3565ir


# """Abell 3570"""
# abell3570imagename = 'abell3570_wfpc2_total.fits'
# abell3570centre = 1047, 1109    # Centre y, x (don't ask)
# abell3570offset = -0.2, 1.1   # Pixel offset off of centre x, y +ve moves to the right and up
# abell3570size = 125
# abell3570angle = np.pi/2 + 0.1
# abell3570eccentricity = 0.58
# abell3570ir = [11.059, 11.098, 10.038, 8.064]
# # Nuker Law Initial Guess
# abell3570ci = 37.51
# abell3570br = 2.53
# abell3570g = 0.00600167
# abell3570t = 1.50764
# abell3570b = 1.5199
# abell3570params = abell3570ci, abell3570br, abell3570g, abell3570t, abell3570b
# # Any Image coreections: rotate 90, image ellipse correction
# abell3570rot = 'yes', 0.9
# abell3570gs = 5
# """Final List: holding all the BCGs individual parameters:::::"""
# abell3570 = abell3570centre, abell3570size, abell3570angle, abell3570eccentricity,\
#             abell3570params, abell3570offset, abell3570gs, abell3570rot, 85, 124.45, abell3570ir


"""Abell 3571"""
a3571imagename = 'Abell3571_08683_9b_wfpc2_f814w_pc_drz.fits'
a3571centre = 478, 526       # Centre y, x (don't ask)
a3571offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3571size = 80
a3571iterations = 60
a3571angle = np.pi / 2 - 0.1
a3571eccentricity = 0.55
a3571ir = [11.254, 11.357, 10.586, 8.757]
# Nuker Law Initial Guess
a3571ci = 0.5174
a3571br = 56.3189
a3571g = -0.0071351
a3571t = 1.6396
a3571b = 2.38808
a3571params = a3571ci, a3571br, a3571g, a3571t, a3571b
# Any Image coreections: rotate 90, image ellipse correction
a3571rot = 'yes', 0.9
a3571gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3571 = a3571centre, a3571size, a3571angle, a3571eccentricity, \
            a3571params, a3571offset, a3571gs, a3571rot, a3571iterations, 132.39, a3571ir


"""Abell 3574"""
a3574imagename = 'Abell3574_06587_08_wfpc2_f555w_pc_drz.fits'
a3574centre = 576, 462       # Centre y, x (don't ask)
a3574offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3574size = 100
a3574iterations = 80
a3574angle = np.pi / 2 - 0.36
a3574eccentricity = 0.4
a3574ir = [9.795, 9.848, 9.37, 8.4]
# Nuker Law Initial Guess
a3574ci = 6.174
a3574br = 7.3189
a3574g = -0.01351
a3574t = 1.596
a3574b = 1.8808
a3574params = a3574ci, a3574br, a3574g, a3574t, a3574b
# Any Image coreections: rotate 90, image ellipse correction
a3574rot = 'no', 0.75
a3574gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3574 = a3574centre, a3574size, a3574angle, a3574eccentricity, \
            a3574params, a3574offset, a3574gs, a3574rot, a3574iterations, 49.59, a3574ir


"""Abell 3656"""
a3656imagename = 'Abell3656_08683_9g_wfpc2_f814w_pc_drz.fits'
a3656centre = 505, 403       # Centre y, x (don't ask)
a3656offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3656size = 100
a3656iterations = 80
a3656angle = np.pi / 2 + 0.5
a3656eccentricity = 0.55
a3656ir = [9.802, 9.843, 9.426, 7.84]
# Nuker Law Initial Guess
a3656ci = 6.174
a3656br = 7.3189
a3656g = -0.01351
a3656t = 1.596
a3656b = 1.8808
a3656params = a3656ci, a3656br, a3656g, a3656t, a3656b
# Any Image coreections: rotate 90, image ellipse correction
a3656rot = 'no', 0.75
a3656gs = 10
"""Final List: holding all the BCGs individual parameters:::::"""
abell3656 = a3656centre, a3656size, a3656angle, a3656eccentricity, \
            a3656params, a3656offset, a3656gs, a3656rot, a3656iterations, 72.90, a3656ir


"""Abell 3676"""
a3676imagename = 'Abell3676_08683_9h_wfpc2_f814w_pc_drz.fits'
a3676centre = 360, 564       # Centre y, x (don't ask)
a3676offset = 0.1, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3676size = 125
a3676iterations = 100
a3676angle = np.pi / 2
a3676eccentricity = 0.2
a3676ir = [11.163, 11.177, 9.069, 7.455]
# Nuker Law Initial Guess
a3676ci = 6.174
a3676br = 7.3189
a3676g = -0.01351
a3676t = 1.596
a3676b = 1.8808
a3676params = a3676ci, a3676br, a3676g, a3676t, a3676b
# Any Image coreections: rotate 90, image ellipse correction
a3676rot = 'yes', 0.9
a3676gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3676 = a3676centre, a3676size, a3676angle, a3676eccentricity, \
            a3676params, a3676offset, a3676gs, a3676rot, a3676iterations, 144.67, a3676ir


"""Abell 3677"""
a3677imagename = 'Abell3677_08683_9i_wfpc2_f814w_pc_drz.fits'
a3677centre = 392, 417       # Centre y, x (don't ask)
a3677offset = -0.4, -0.4      # Pixel offset off of centre x, y +ve moves to the right and up
a3677size = 100
a3677iterations = 100
a3677angle = np.pi / 2 + 0.81
a3677eccentricity = 0.72
a3677ir = [11.879, 11.891, 10.352, 8.268]
# Nuker Law Initial Guess
a3677ci = 6.174
a3677br = 7.3189
a3677g = -0.01351
a3677t = 1.596
a3677b = 1.8808
a3677params = a3677ci, a3677br, a3677g, a3677t, a3677b
# Any Image coreections: rotate 90, image ellipse correction
a3677rot = 'no', 0.9
a3677gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3677 = a3677centre, a3677size, a3677angle, a3677eccentricity, \
            a3677params, a3677offset, a3677gs, a3677rot, a3677iterations, 163.35, a3677ir


"""Abell 3698"""
a3698imagename = 'Abell3698_08683_9j_wfpc2_f814w_pc_drz.fits'
a3698centre = 510, 542       # Centre y, x (don't ask)
a3698offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3698size = 125
a3698iterations = 100
a3698angle = np.pi / 2 + 0.15
a3698eccentricity = 0.72
a3698ir = [10.195, 10.23, 9.411, 7.657]
# Nuker Law Initial Guess
a3698ci = 39.174
a3698br = 6.3189
a3698g = -0.2991351
a3698t = 0.86896
a3698b = 1.8908
a3698params = a3698ci, a3698br, a3698g, a3698t, a3698b
# Any Image coreections: rotate 90, image ellipse correction
a3698rot = 'yes', 0.9
a3698gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3698 = a3698centre, a3698size, a3698angle, a3698eccentricity, \
            a3698params, a3698offset, a3698gs, a3698rot, a3698iterations, 78.28, a3698ir


"""Abell 3716"""
abell3716imagename = 'abell3716_PC_f814w.fits'
abell3716centre = 397, 423    # Centre y, x (don't ask)
abell3716offset = 0.5, -15   # Pixel offset off of centre x, y +ve moves to the right and up
abell3716size = 100
abell3716iterations = 70
abell3716angle = np.pi/2 + np.pi/4 + 0.05
abell3716eccentricity = 0.42
abell3716ir = [11.427, 11.427, 10.747, 8.737]
# Nuker Law Initial Guess
abell3716ci = 1.97415
abell3716br = 10.3078
abell3716g = -0.02386
abell3716t = 2.0459
abell3716b = 1.37247
abell3716params = abell3716ci, abell3716br, abell3716g, abell3716t, abell3716b
# Any Image coreections: rotate 90, image ellipse correction
abell3716rot = 'no', 0.9
abell3716gs = 8
"""Final List: holding all the BCGs individual parameters:::::"""
abell3716 = abell3716centre, abell3716size, abell3716angle, abell3716eccentricity,\
            abell3716params, abell3716offset, abell3716gs, abell3716rot, abell3716iterations, 157.65, abell3716ir


"""Abell 3733"""
a3733imagename = 'Abell3733_08683_9j_wfpc2_f814w_pc_drz.fits'
a3733centre = 557, 613       # Centre y, x (don't ask)
a3733offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3733size = 125
a3733iterations = 100
a3733angle = np.pi / 2 + 0.1
a3733eccentricity = 0.4
a3733ir = [11.332, 11.394, 10.432, 7.793]
# Nuker Law Initial Guess
a3733ci = 1.4174
a3733br = 13.3189
a3733g = -0.0091351
a3733t = 2.7596
a3733b = 1.41808
a3733params = a3733ci, a3733br, a3733g, a3733t, a3733b
# Any Image coreections: rotate 90, image ellipse correction
a3733rot = 'yes', 0.75
a3733gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3733 = a3733centre, a3733size, a3733angle, a3733eccentricity, \
            a3733params, a3733offset, a3733gs, a3733rot, a3733iterations, 134.79, a3733ir


"""Abell 3736"""
a3736imagename = 'Abell3736_08683_9m_wfpc2_f814w_pc_drz.fits'
a3736centre = 597, 525       # Centre y, x (don't ask)
a3736offset = 0.1, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3736size = 100
a3736iterations = 100
a3736angle = np.pi / 2 + 0.45
a3736eccentricity = 0.64
a3736ir = [11.14, 11.191, 10.63, 8.667]
# Nuker Law Initial Guess
a3736ci = 3.174
a3736br = 21.3189
a3736g = -0.07351
a3736t = 1.0016
a3736b = 2.054808
a3736params = a3736ci, a3736br, a3736g, a3736t, a3736b
# Any Image coreections: rotate 90, image ellipse correction
a3736rot = 'yes', 0.9
a3736gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3736 = a3736centre, a3736size, a3736angle, a3736eccentricity, \
            a3736params, a3736offset, a3736gs, a3736rot, a3736iterations, 171.65, a3736ir


"""Abell 3742"""
a3742imagename = 'Abell3742_05910_04_wfpc2_f814w_pc_drz.fits'
a3742centre = 511, 588       # Centre y, x (don't ask)
a3742offset = -0.5, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3742size = 100
a3742iterations = 100
a3742angle = np.pi / 2 + 0.72
a3742eccentricity = 0.68
a3742ir = [9.912, 9.997, 9.432, 8.432]
# Nuker Law Initial Guess
a3742ci = 10.174
a3742br = 10.3189
a3742g = -0.01351
a3742t = 1.596
a3742b = 1.8808
a3742params = a3742ci, a3742br, a3742g, a3742t, a3742b
# Any Image coreections: rotate 90, image ellipse correction
a3742rot = 'no', 0.75
a3742gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3742 = a3742centre, a3742size, a3742angle, a3742eccentricity, \
            a3742params, a3742offset, a3742gs, a3742rot, a3742iterations, 62.19, a3742ir


"""Abell 3744"""
a3744imagename = 'Abell3744_08683_9o_wfpc2_f814w_pc_drz.fits'
a3744centre = 498, 553       # Centre y, x (don't ask)
a3744offset = -0.3, -0.3      # Pixel offset off of centre x, y +ve moves to the right and up
a3744size = 100
a3744iterations = 70
a3744angle = np.pi / 2 - 0.25
a3744eccentricity = 0.37
a3744ir = [10.869, 10.93, 10.059, 8.665]
# Nuker Law Initial Guess
a3744ci = 10.174
a3744br = 10.3189
a3744g = -0.01351
a3744t = 1.596
a3744b = 1.8808
a3744params = a3744ci, a3744br, a3744g, a3744t, a3744b
# Any Image coreections: rotate 90, image ellipse correction
a3744rot = 'no', 0.9
a3744gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3744 = a3744centre, a3744size, a3744angle, a3744eccentricity, \
            a3744params, a3744offset, a3744gs, a3744rot, a3744iterations, 136.58, a3744ir


"""Abell 3747"""
a3747imagename = 'Abell3747_08683_9p_wfpc2_f814w_pc_drz.fits'
a3747centre = 535, 456       # Centre y, x (don't ask)
a3747offset = 0.7, -0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a3747size = 100
a3747iterations = 100
a3747angle = np.pi / 2 + 0.75
a3747eccentricity = 0.75
a3747ir = [10.792, 10.853, 10.332, 8.485]
# Nuker Law Initial Guess
a3747ci = 30.174
a3747br = 3.3189
a3747g = -0.361351
a3747t = 0.9596
a3747b = 1.8808
a3747params = a3747ci, a3747br, a3747g, a3747t, a3747b
# Any Image coreections: rotate 90, image ellipse correction
a3747rot = 'yes', 0.9
a3747gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell3747 = a3747centre, a3747size, a3747angle, a3747eccentricity, \
            a3747params, a3747offset, a3747gs, a3747rot, a3747iterations, 112.47, a3747ir


"""Abell 4038"""
a4038imagename = 'Abell4038_08683_9r_wfpc2_f814w_pc_drz.fits'
a4038centre = 467, 509       # Centre y, x (don't ask)
a4038offset = 0.4, 0.4      # Pixel offset off of centre x, y +ve moves to the right and up
a4038size = 100
a4038iterations = 100
a4038angle = np.pi / 2 - 0.6
a4038eccentricity = 0.5
a4038ir = [10.792, 10.853, 10.332, 8.485]
# Nuker Law Initial Guess
a4038ci = 6.174
a4038br = 7.3189
a4038g = -0.01351
a4038t = 1.596
a4038b = 1.8808
a4038params = a4038ci, a4038br, a4038g, a4038t, a4038b
# Any Image coreections: rotate 90, image ellipse correction
a4038rot = 'yes', 0.75
a4038gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell4038 = a4038centre, a4038size, a4038angle, a4038eccentricity, \
            a4038params, a4038offset, a4038gs, a4038rot, a4038iterations, 108.51, a4038ir


"""Abell 4049"""
a4049imagename = 'Abell4049_08683_9s_wfpc2_f814w_pc_drz.fits'
a4049centre = 537, 562      # Centre y, x (don't ask)
a4049offset = -0.3, 0.1      # Pixel offset off of centre x, y +ve moves to the right and up
a4049size = 100
a4049iterations = 100
a4049angle = np.pi / 2 - 0.3
a4049eccentricity = 0.3
a4049ir = [10.549, 10.587, 9.326, 7.225]
# Nuker Law Initial Guess
a4049ci = 12.174
a4049br = 10.3189
a4049g = -0.01351
a4049t = 1.596
a4049b = 1.8808
a4049params = a4049ci, a4049br, a4049g, a4049t, a4049b
# Any Image coreections: rotate 90, image ellipse correction
a4049rot = 'no', 0.9
a4049gs = 10
"""7inal List: holding all the BCGs individual parameters:::::"""
abell4049 = a4049centre, a4049size, a4049angle, a4049eccentricity, \
            a4049params, a4049offset, a4049gs, a4049rot, a4049iterations, 108.85, a4049ir


"""Abell 4059"""
abell4059imagename = 'images/a4059.fits'
abell4059centre = 651, 1006    # Centre y, x (don't ask)
abell4059offset = 0.5, -3   # Pixel offset off of centre x, y +ve moves to the right and up
abell4059size = 150
abell4059iterations = 140
abell4059angle = np.pi/2 - 0.26
abell4059eccentricity = 0.6
abell4059ir = [11.318, 11.396, 10.431, 8.732]
# Nuker Law Initial Guess
abell4059ci = 5.2204
abell4059br = 8.523
abell4059g = -0.10572
abell4059t = 1.37498
abell4059b = 1.27893
abell4059params = abell4059ci, abell4059br, abell4059g, abell4059t, abell4059b
# Any Image coreections: rotate 90, image ellipse correction
abell4059rot = 'yes', 0.8
abell4059gs = 8
"""Final List: holding all the BCGs individual parameters:::::"""
abell4059 = abell4059centre, abell4059size, abell4059angle, abell4059eccentricity,\
            abell4059params, abell4059offset, abell4059gs, abell4059rot, abell4059iterations, 174.84, abell4059ir


galaxylist = abell76, abell119, abell147, abell160, abell168, abell189, abell193, abell195, abell260, abell262,\
             abell295, abell347, abell376, abell397, abell419, abell496, abell533, abell548, abell634, \
             abell671, abell779, abell912, abell999, abell1016, abell1060, abell1142, abell1177, abell1228, abell1308,\
             abell1314, abell1367, abell1631, abell1656, abell1795, abell1836, abell1983, abell2040, abell2052, \
             abell2147, abell2162, abell2197, abell2247, abell2572, abell2589, abell2593, abell2634, abell2657, \
             abell2666, abell2877, abell3144, abell3193, abell3376, abell3395, abell3526, abell3528, abell3532, \
             abell3554, abell3556, abell3558, abell3559, abell3562, abell3564, abell3565, abell3571, \
             abell3574, abell3656, abell3676, abell3677, abell3698, abell3716, abell3733, abell3736, abell3742, \
             abell3744, abell3747, abell4038, abell4049, abell4059
