# teachers send in pictures of IDs, along with information about their schools 
# cards are compared (ignore faculty feedback feature for now) 

# question: will the system process one image at a time? (this is easier for us)

import cv2
import os
import image_similarity_measures
from sys import argv
from image_similarity_measures.quality_metrics import rmse, ssim, sre

# return True or False (are the ID cards similar or not)
def similar(path_to_img, school_name, city, country):
    if (os.path.isdir('/Users/soulie/hackbca/refucation/images/verified/teacher_id_cards/' + school_name + '_' + city + '_' + country) is False):
        # TODO: if no such school is yet registered, run real-school-test
        # Use SQLite
        return False
    else: 
        # credit to https://betterprogramming.pub/how-to-measure-image-similarities-in-python-12f1cb2b7281 
        # not tested yet 
        test_img = cv2.imread(path_to_img)

        ssim_measures = {}
        rmse_measures = {}
        sre_measures = {}

        scale_percent = 100 # percent of original img size
        width = int(test_img.shape[1] * scale_percent / 100)
        height = int(test_img.shape[0] * scale_percent / 100)
        dim = (width, height)

        data_dir = '/Users/soulie/hackbca/refucation/images/verified/teacher_id_cards/' + school_name + '_' + city + '_' + country

        for file in os.listdir(data_dir):
            img_path = os.path.join(data_dir, file)
            data_img = cv2.imread(img_path)
            resized_img = cv2.resize(data_img, dim, interpolation = cv2.INTER_AREA)
            ssim_measures[img_path]= ssim(test_img, resized_img)
            rmse_measures[img_path]= rmse(test_img, resized_img)
            sre_measures[img_path]= sre(test_img, resized_img)

        # fix this part so that it gets the average similarity, 90+ percent similarity is good 
        """
        def calc_closest_val(dict, checkMax):
            result = {}
            if (checkMax):
                closest = max(dict.values())
            else:
                closest = min(dict.values())
                    
            for key, value in dict.items():
                print("The difference between ", key ," and the original image is : \n", value)
                if (value == closest):
                    result[key] = closest
                    
            print("The closest value: ", closest)	    
            print("######################################################################")
            return result
        
        ssim = calc_closest_val(ssim_measures, True)
        rmse = calc_closest_val(rmse_measures, False)
        sre = calc_closest_val(sre_measures, True)

        print("The most similar according to SSIM: " , ssim)
        print("The most similar according to RMSE: " , rmse)
        print("The most similar according to SRE: " , sre)
        """