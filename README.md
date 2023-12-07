<h1>Automation scripts</h1>

This repository contains Python scripts automating certain workflows. <br>
<ul>
<li>
    <i><strong>DocToPdfConverter.py</strong></i>: As the name suggests, 
    this script automatically converts Word documents 
    in a given folder specified by the absolute path to PDF. To use the script, an installation of Microsoft Word
    and a valid license is required.

    The necessity came up when applying to lots of internships, with each application requiring a cover letter. Opening each word document with the company-/position-specific cover letter and saving it as a PDF was a time-consuming process, so automating it made sense. 
</li>
<li>
    <i><strong>multi-repo-clone.sh</strong></i>: This bash script was written for simplifying `git clone` for a large amount of repositories. 
    
    The necessity came up when working on a large-scale project with a microservice architecture. Each microservice had its own repository with about 50 services in total, so cloning all repos was a tedious and human error-prone process.
</li>
</ul>
