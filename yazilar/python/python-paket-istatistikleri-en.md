<!-- 
.. description: Some descriptive statistics about packages on PyPI.
.. date: 2013/10/18 15:30
.. title: Python Package Statistics
.. slug: python-package-statistics
-->

I am writing this in order to give some descriptive statistics about Python Packages in PyPI. I crawled 34968 indiviual
package pages on Python package index. I could extract data from 34923 of them. PyPI reports 35813 packages, but some of them
are different versions of same packages. I preferred working with latest versions.

Why did I do this? Curiosity and spare time...<!-- TEASER_END -->

## Package Size

Most packages provide a download section in their PyPI page. I got data from first file listed in download section. Here are the
biggest packages on PyPI:

 1. b2gpopulate (36MB)
 2. ajenti (35MB)
 3. FinPy (29MB)
 4. django-dojo (28MB)
 5. QSTK (27MB)

Total sizes on packages in PyPI amounted to 4.2 GB. Average package size is 161 KB and standard deviation is 1MB.

I normalized values using `1MB = 1024KB` and `1KB = 1024 B`.

## Most Required Packages

I designated a requiredness score for individual packages. This score works like this; if package a needs package b, and package b
needs package c, in that case, c gets score of 2, and b gets score of 1, because c has directly or indirectyl have 2 packages
requiring it. I have used *Requires* section of package pages to calculate this. Some packages doesn't provide this information and
some have mistakes in this section like spelling errors. However, results seems representative of real requiredness value.

 1. numpy (1500)
 2. django (860)
 3. scipy (555)
 4. python (425)
 5. matplotlib (370)
 6. simplejson (310)
 7. requests (310)
 8. pil (275)
 9. pyyaml (265)
 10. lxml (255)
 
Some packages appeares to have specified *python* as a required package.

## Downloads

Every package provides daily, weekly and monthly download data on their page. I collected these numbers in early morning of 18 october 2013.
Here are most downloaded packages and some statistics.

### Daily

 1. distribute (67 417)
 2. setuptools (52 184)
 3. requests (50 486)
 4. ssl (50 201)
 5. certifi (49 738)
 
total: 1 880 974, average: 54, standard deviation: 900.

### Weekly

 1. distribute (445 006)
 2. setuptools (414 556)
 3. ssl (379 201)
 4. certifi (378 729)
 5. wincertstore (375 158)
 
total 14 097 027, average: 403.6, standard deviation: 6 425.

### Monthly

 1. distribute (1 743 309)
 2. setuptools (1 607 116)
 3. certifi (1 546 749)
 4. ssl (1 537 270)
 5. wincertstore (1 532 424)
 
total: 53 281 293, average: 1525.7, standard deviation: 25058.7

## Number of Lines of Python Code

I selected random sample of 30 packages using `random.sample()`. I downloaded source files and counted number of non-empty lines in python
files (excluding setup.py). Minimum and maximum lines were 2 and 47 453 respectively. Number of lines averaged to 2212.6 lines per package
and standard deviation was 8729.7. 95% confidence interval for population mean had upper limit of 5336.4 and lower limit was negative
number. Therefore, we can estimate that there are `2212 * 35813 = 79 239 844` lines of Python code on package index. As an upper limit,
we can use `5336.4 * 35813 = 191 112 493` lines of code with 95% confidence.

## Data

[Packages meta data](https://docs.google.com/file/d/0B_hwkDj0Is2Wdkl0S21kN29YUVk/edit?usp=sharing) (5 MB rar file) can be
accessed through google drive. You will get a pickled Python dictionary (around 23 MB) when you extract rar file. To load data:

	:::python
	from pickle import load

	with open("all_in_one") as d:
		package_metas = load(d)

Veys of the `package_metas` will be lowercase package names. Values are dictionaries of package meta data. Most packages will at least
provide `packagename`, `daily`, `weekly`, `monthly`, `Author`, `Home Page` fields, however, some might not provide this info. It is
because when I encountered unknown packages during determination of requiredness_score, I added unknown packages to this dictionary.

Most packages will also provide `filename`, `filetype`, `pyversion`, `uploaded` and `size` data.

Other keys of per package dictionaries depend on individual packages.