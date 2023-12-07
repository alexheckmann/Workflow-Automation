<h1>Automation scripts</h1>

This repository contains Python scripts automating certain workflows. <br>
<ul>
<li>
    <i><strong>DocToPdfConverter.py</strong></i>: As the name suggests, 
    this script automatically converts Word documents 
    in a given folder specified by the absolute path to PDF. To use the script, an installation of Microsoft Word
    and a valid license is required. The necessity came up when applying to lots of internships, with each application requiring a cover letter. Opening each word document with the company-/position-specific cover letter and saving it as a PDF was a time-consuming process, so automating it made sense. 
</li>
<li>
    <i><strong>multi-repo-clone.sh</strong></i>: This bash script was written for simplifying `git clone` for a large amount of repositories. The necessity came up when working on a large-scale project with a microservice architecture. Each microservice had its own repository with about 50 services in total, so cloning all repos was a tedious and human error-prone process.
</li>
<li>
    <i><strong>create_code_appendix.sh</strong></i>: This bash script was written for simply copying all code of a given folder. It recursively goes into each folder that is not excluded and copies the content of each found file into a single file. This txt file then gets converted into PDF. The necessity for my master thesis, as my uni requested to put all my code into the appendix as a PDF. The code I wrote for the thesis was a deeply nested Next.js application with ~10000 Lines of Code in 139 different .ts & .tsx files, hence manually copying every single file content would be a tiresome and probably faulty process.
</li>
</ul>
