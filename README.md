# Computer Embroidery Experiment
### Resources
* [OpenCV](http://opencv.org/)
* [NumPy](http://numpy.org)
* [ColorWeave](https://pypi.python.org/pypi/colorweave/0.1)

### About
This is project is an experiment aimed at understanding a computers ability to imitate creativity and inspiration through turning a piece of art into an embroidery pattern. The art was analyzed in python, interpreted into context-free art over 2 iterations and then all interpretations were compared to the original image using similar analysis.  A final interpretation was chosen, and the final embroidery image was processed in Embroidery software and embroidered on muslin fabric.

### Installation / Process
Begin by downloading an image of your choice and saving it (I recommend saving it in the main directory).  Run the analyze-image.py script on the downloaded image.
This script runs OpenCV image analytics on the input file, determines the numbers of circles and lines, and the average angle in the images, and uses these metrics to edit a basic Context Free Art design file. It also detects the 3 most salient colors in the image to apply to the output later. It then saves a Context Free Art (CFA) design file in the out/cfa directory as well as a color file in the out/render directory.  
In order to iterate the program on the original output, you need to save various renderings of the design file. You can either open the design file in CFA to render and save multiple times, or run a Windows or Linux command version of CFA.  I saved .png and .svg files of 25 renders of the output.  .pngs were saved in out/img and .svgs were saved in out/render.  I recommend numbering each png/svg rendering to organize the files.
To Re-analyze the output images, run the analyze-output.py file.  This will analyze all of the output png’s in the same way the input images were analyzed. Again, it puts them in the out/cfa folder under the same name as the saved .png file. You should now render each of the files and save a .png and .svg in out/img and out/render respectively.
Next, to compare the various output images to the original image, the program compare-values.py should be run on the original image. This will compare the analytics of the original image to every output image in the img directory.  Basically, it compares the difference in the number of lines, number of circles, and average angle in the original image to each output.  This will print the most similar image and the difference between the original image and its most similar image.
You can then go into img/render and run change-color.py on the image name printed by the last script and the color file for the original image. This will output a new .svg prefixed with “final-“ with the colors adjusted to match the original image’s salient colors. 

### Outcome
After applying this process to 5 works of art, I was able to create 5 embroidery files similar to the original images.  I rendered each design file 25 times and compared the original images to 50 outputs.  The computer-selected output images were generally closer than 100 points apart, given the number of lines, circles, and average angles different.  One outlier had a most similar image with a distance of 1400.  The lowest difference was 27.  I believe that with more iterations and renderings, a closer match could be found.
