# GitHub README SEO: Data Analysis of What Makes Repos Rank

<!-- slug: github-readme-seo-analysis -->
<!-- Title chars = 57 chars -->

 <!-- LATER: Badges (Python, Pandas, Numpy?, Matplotlib, Seaborn?) -->
 <!-- Google: "sample readme for a jupyter notebook data analysis project" for good boilerplate -->

This project performs a GitHub README SEO Analysis using Jupyter Notebook and data from GitHub Explore & Google to determine the metrics needed to rank in the SERPS.

> [!NOTE]
> I am new to Data Analysis and Jupyter Notebook. I am in the early stages of this analysis and it will take me a long time to finish unless I get help.

<!-- Intro paraagraph = 171 chars -->

<!--
   ✅ = Section done
   📌 = Section not done
 -->

<br>

## Overview

<!-- ✅ -->

The goal of this project is to understand why certain GitHub repositories rank in Google & GitHub Explore search results (SERPs) while others do not.

I collected a dataset of repositories using 46 search phrases and recorded both Google rankings and GitHub Explore rankings. For each repository, I also gathered metrics related to README content, repository activity, and available SEO data like titles and meta descriptions.

<!-- The analysis focuses on identifying patterns between these factors and ranking performance. In particular, it looks at whether common practices, such as having a clear README structure, or a descriptive introduction is associated with higher visibility. -->

The end goal is to turn these findings into practical insights that can be applied to improve repository discoverability. This includes refining my own repositories as well as sharing useful patterns, the dataset, and the results with other developers.

<br>

<h2 id="back-to-top">Table of Contents</h1>

1. [Key Questions](#key-questions)
1. [Key Findings](#key-findings)
1. [Data Sources](#data-sources)
1. [Methodology](#methodology)
1. [Visualizations](#visualizations)
1. [Data Dictionary](#data-dictionary)
1. [Project Structure](#project-structure)
1. [Tech Stack](#tech-stack)
1. [Installation](#installation)
1. [Usage](#usage)
1. [Future Improvements](#future-improvements)
1. [Ai Usage](#ai-usage)
1. [Acknowledgments](#acknowledgments)
1. [Contributing](#contributing)
1. [License](#license)

<br>

## Key Questions

<!-- 📌 -->

> 🚧 Section under construction (Too many questions?)

- Which factors are associated with a repository appearing in Google search results (SERPs)?
- Which factors are associated with higher rankings within Google SERPs and GitHub Explore?
- How closely do GitHub Explore rankings align with Google search rankings?
- Is there a relationship between README structure (e.g., H1 usage, table of contents, introduction) and ranking?
- Does the presence of a clear, descriptive introduction impact visibility or ranking?
- Do content characteristics (e.g., word count, links, images) correlate with ranking performance?
- Do broken or low-quality links (e.g., `http://localhost`) correlate with lower rankings?
- Which repository features within a developer's control appear most associated with higher rankings?
- How often do repositories use default titles (e.g., username/repository) versus descriptive titles? What causes that difference?
- Is GitHub "About" text reused in Google SEO titles or meta descriptions?

### Specific questions (remove this section later maybe)

1. Does about_text get reused in:
   - seo_title
   - meta_description
2. Do SERP fields reuse leading substrings of:
   - about text
   - README title
   - Intro paragraphs
3. Does Google fall back to:
   - username/repo for SEO Title when no usable text exists?

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Key Findings

<!-- 📌 -->

Summarize the most important insights discovered during the analysis.

> 🚧 Nothing yet

<!-- Example:

- Homes within 1 mile of downtown were 35% more expensive.
- Temperature had a strong correlation with bike rentals.
- Product category X generated 48% of revenue. -->

### 🔍 Google SERP Insights

- 🚧 Nothing yet (this sub-section may not be needed)

### 🔍 GitHub Explore Insights

- 🚧 Nothing yet (this sub-section may not be needed)

<!-- ### Key Differences -->

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Data Sources

<!-- ✅ -->

The dataset for this project was created manually using a combination of Google search results and GitHub Explore.

Two primary data files were generated:

- `data/all_metrics.csv`
  Contains repository-level data, including README structure and content metrics (e.g., headings, word count, links, images), repository metadata (stars, forks, contributors), and SEO-related fields where available.
- `data/search_ranks.csv`
  Contains ranking data for each repository across multiple search phrases.

These datasets are joined using the `user_reponame` field to enable combined analysis of repository features and ranking performance (see `merged_data.csv`).

### 🗃️ APIs Used

- GitHub API: Used in `github_api.py` to collect repository metadata. This significantly reduced the need for manual data collection and improved consistency across records. More code could be added to get additional repo and README metrics.

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Methodology

<!-- 📌 -->

> 🚧 Section under construction

- Data collection: search phrases on Google and GitHub Explore
- Data Processing and Transformation: ???
- Data Analysis: ???

> Repositories without a README file were excluded from content-based analysis where applicable, as key metrics (e.g., word count, structure, and links) could not be derived.

### 🗃️ Data Collection

<!-- ✅ Use the sub-sections below only if they improve clarity -->
<!-- ✅ -->

Data was collected from both Google search results (SERPs) and GitHub Explore using a set of 46 targeted search phrases. A custom script (`github_api.py`) was used to retrieve repository metadata via the GitHub API.

For each search phrase:

- The top 10 results from GitHub Explore were recorded.
- The top results from Google search were collected (cutoff at 50), including variations where the term "github" was appended to the query.

This process resulted in:

- 335 unique repositories
- 455 total ranking records across all search phrases

### 🔧 Data Processing and Transformation

<!-- 📌 -->

> 🚧 Section under construction

- Processing: organizing / filtering / restructuring, selecting columns, grouping/sorting, "prepare for analysis"
- Transformation: creating new variables/features, aggregations, encoding / scaling, "change the data into new forms"

### 📊 Data Analysis

<!-- 📌 -->

> 🚧 Section under construction

> Visualize relationships between fields and rank positions to derive insights

The analysis focused on identifying relationships between repository and README features and their ranking positions in both Google and GitHub search results.

<!-- Comparisons were made between top-ranking and lower-ranking repositories to identify patterns and potential ranking factors. -->

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Visualizations

<!-- 📌 -->

> 🚧 Section under construction

Show key charts or plots.

Include screenshots of graphs from the notebook.

Explain what each chart demonstrates.

<br>

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

## Data Dictionary

<!-- ✅ -->

Here are all the fields in `merged_data.csv`:

<!-- Should it be labeled Dataset instead? Should I add all the fields? -->
<!-- Should I explain why I have fields like has_blog? -->

<details>
  <summary><strong>Data Dictionary fields</strong></summary>
   <table>
      <thead>
         <tr>
            <th>Field Name</th>
            <th>Data Type</th>
            <th>Description</th>
         </tr>
      </thead>
      <tbody>
         <tr>
            <td>user_reponame</td>
            <td>str</td>
            <td>The repo: <code>user_name/repo_name</code></td>
         </tr>
         <tr>
            <td>search_phrase</td>
            <td>str</td>
            <td>The search phrase used</td>
         </tr>
         <tr>
            <td>explore_rank</td>
            <td>int64</td>
            <td>Position in GitHub EXplore results</td>
         </tr>
         <tr>
            <td>google_rank</td>
            <td>int64</td>
            <td>Position in Google SERPs</td>
         </tr>
         <tr>
            <td>source</td>
            <td>str</td>
            <td>
               <ul>
                  <li>Google SERPs</li>
                  <li>Google SERPs with "github" appended to search phrase</li>
                  <li>GitHub Explore results</li>
               </ul>
            </td>
         </tr>
         <tr>
            <td>1st_el</td>
            <td>str</td>
            <td>1st text element in README</td>
         </tr>
         <tr>
            <td>2nd_el</td>
            <td>str</td>
            <td>2nd text element in README</td>
         </tr>
         <tr>
            <td>3rd_el</td>
            <td>str</td>
            <td>3rd text element in README</td>
         </tr>
         <tr>
            <td>h1_ct</td>
            <td>int64</td>
            <td># of H1 elements</td>
         </tr>
         <tr>
            <td>h2_ct</td>
            <td>int64</td>
            <td># of H2 elements</td>
         </tr>
         <tr>
            <td>h3_ct</td>
            <td>int64</td>
            <td># of H3 elements</td>
         </tr>
         <tr>
            <td>toc</td>
            <td>int64</td>
            <td>
               <ul>
                  <li>0 = No table of contents</li>
                  <li>1 = Table of contents present</li>
               </ul>
            </td>
         </tr>
         <tr>
            <td>images</td>
            <td>int64</td>
            <td># of images in README</td>
         </tr>
         <tr>
            <td>alt_text_ct</td>
            <td>int64</td>
            <td># of images with alt text</td>
         </tr>
         <tr>
            <td>code_blocks</td>
            <td>int64</td>
            <td># of code blocks in README</td>
         </tr>
         <tr>
            <td>internal_links</td>
            <td>int64</td>
            <td># of links to repo files</td>
         </tr>
         <tr>
            <td>external_links</td>
            <td>int64</td>
            <td># of links to external sites or repos</td>
         </tr>
         <tr>
            <td>live_link</td>
            <td>int64</td>
            <td>
               <ul>
                  <p>My opinion on the quality of the README</p>
                  <li>0 = No link to live deploy</li>
                  <li>1 = Link to live deploy in sidebar</li>
               </ul>
            </td>
         </tr>
         <tr>
            <td>watchers</td>
            <td>int64</td>
            <td># of repo watchers</td>
         </tr>
         <tr>
            <td>contributors</td>
            <td>int64</td>
            <td># of repo contributors</td>
         </tr>
         <tr>
            <td>rank</td>
            <td>int64</td>
            <td>
               <ul>
                  <li>1 = Bad</li>
                  <li>2 = Good/okay</li>
                  <li>3 = Very Good</li>
               </ul>
            </td>
         </tr>
         <tr>
            <td>type</td>
            <td>str</td>
            <td>My main classification of the repo</td>
         </tr>
         <tr>
            <td>type2</td>
            <td>str</td>
            <td>My sub-class for the repo</td>
         </tr>
         <tr>
            <td>word_count</td>
            <td>int64</td>
            <td>README word count</td>
         </tr>
         <tr>
            <td>forks</td>
            <td>int64</td>
            <td># of forks for repo</td>
         </tr>
         <tr>
            <td>stars</td>
            <td>int64</td>
            <td># of stars for repo</td>
         </tr>
         <tr>
            <td>topics</td>
            <td>int64</td>
            <td># of topics in sidebar</td>
         </tr>
         <tr>
            <td>seo_title</td>
            <td>str</td>
            <td>The title from the Google SERPs</td>
         </tr>
         <tr>
            <td>meta_desc</td>
            <td>str</td>
            <td>The description from the Google SERPs</td>
         </tr>
         <tr>
            <td>title_text</td>
            <td>str</td>
            <td>The About text from the repo sidebar</td>
         </tr>
         <tr>
            <td>intro_len</td>
            <td>int64</td>
            <td>The length of the intro text if good_intro = 1</td>
         </tr>
         <tr>
            <td>good_intro</td>
            <td>int64</td>
            <td>
               <ul>
                  <p>My judgement based on the quality & length of the text at the top of the repo<p>
                  <li>0 = No</li>
                  <li>1 = Yes</li>
               </ul>
            </td>
         </tr>
         <tr>
            <td>primary_lang</td>
            <td>str</td>
            <td>Language used in search phrase</td>
         </tr>
         <tr>
            <td>yr</td>
            <td>int64</td>
            <td># of years since last update</td>
         </tr>
         <tr>
            <td>mo</td>
            <td>int64</td>
            <td># of months since last update</td>
         </tr>
         <tr>
            <td>wk</td>
            <td>int64</td>
            <td># of weeks since last update</td>
         </tr>
         <tr>
            <td>has_blog</td>
            <td>int64</td>
            <td>
               <ul>
                  <li>0 = No blog/website</li>
                  <li>1 = Blog/website</li>
                  <li>2 = Links to Hashnode, Medium, etc.</li>
               </ul>
            </td>
         </tr>
      </tbody>
   </table>
</details>

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Project Structure

<!-- 📌 -->

> Current structure as of 4-19-2026

```py
 github-readme-seo-analysis/
│
├── .github/                     # Issue & PR templates
│
├── data/                        # All datasets used in analysis
│   ├── all_metrics.csv          # Repo & README metrics
│   ├── merged_data.csv          # The 2 csv files merged
│   └── search_ranks.csv         # Google and GitHub Explore ranks + search phrases
│
├── notebooks/                   # Jupyter notebooks for analysis
│   ├── 01-eda_overview.ipynb
│   ├── 02-google_rank.ipynb
│   └── 03-explore_rank.ipynb
│
├── src/                         # Python scripts (data collection, processing)
│   └── github_api.py
│
├── venv/                        # ???
│
├── visuals/                     # Charts/images for README (optional but recommended)
│
├── .env                         # API keys
├── .env.example
├── .gitignore
├── CONTRIBUTING.md
├── CODE_OF_CONDUCT.md
├── LICENSE                      # Add later
├── README.md                    # Project overview (SEO target)
└── requirements.txt
```

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Tech Stack

<!-- ✅ -->

| Tool                                     | Version |
| :--------------------------------------- | :------ |
| [Python](https://www.python.org/)        | 3.14.0  |
| [Jupyter Notebook](https://jupyter.org/) | 7.4.5   |
| [Pandas](https://pandas.pydata.org/)     | 3.0.1   |
| [Matplotlib](https://matplotlib.org/)    | 3.10.6  |
| [Seaborn](https://seaborn.pydata.org/)   | 0.13.2  |
| [NumPy](https://numpy.org/)              | 2.4.3   |

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Installation

<!-- ✅ -->

Follow these steps to set up the project locally.

1. Clone the repository:

   ```bash
   git clone https://github.com/Kernix13/github-readme-seo-analysis
   cd github-readme-seo-analysis
   ```

2. Create a Virtual Environment

   ```bash
   # Linux/Mac Command
   python3 -m venv venv

   # GitBash Command (Windows)
   python -m venv venv
   ```

3. Activate the virtual environment

   ```bash
   # Linux/Mac Command
   source venv/bin/activate

   # GitBash Command (Windows)
   source venv/Scripts/activate
   ```

4. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

### ⚡ Quick Start (Windows)

```sh
git clone https://github.com/yourusername/github-readme-seo-analysis.git
cd github-readme-seo-analysis
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### ⚡ Quick Start (Linux / macOS)

```sh
git clone https://github.com/yourusername/github-readme-seo-analysis.git
cd github-readme-seo-analysis
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Usage

<!-- ✅ -->

<!-- Do I include notes about using `github_api.py` here? And what about mentioning Anaconda or is that bad? -->

1. Start Jupyter:

   ```sh
   # recommended:
   jupyter lab
   # or, if you prefer the classic interface:
   jupyter notebook
   ```

2. Open the `.ipynb` notebook files in the browser interface and run the cells
3. Deactivate the virtual environment when done

   ```sh
   deactivate
   ```

**Note**: If you are using Anaconda or another environment manager, you can open the notebook using your preferred tool (e.g., Anaconda Navigator or jupyter lab) after installing the required dependencies.

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Future Improvements

<!-- 📌 -->

> 🚧 Section under construction

- I need more repos/examples and the need for contributors (only 337 repos)
- Maybe a related Web Dev project that converts your README to HTML then does an SEO analysis and Accessibility check with output that shows what you need and/or suggestions? Or run it through Lighthouse

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## AI Usage

<!-- 📌 -->

> 🚧 Section under construction

I am in the early stages of learning Python, so I used ChatGPT to write the code in `src/github_api.py` to speed up the process of collecting metrics for the repos. There is a list where you enter the username/reponame and the returns values are:

- README word count
- Number of repo forks
- Number of repo stars
- Number of repo topics
- About text

There are other fields I may be able to get but for now I get the rest of the metrics by going to the repo.

Repo-level metrics I would watch to get using the GitHub API are:

- Whether there is a live link in the sidebar or not
- The number of watchers
- The primary language IF it is part of the search query
- the year, month, week, or day since last update

README-level metrics I would watch to get using the GitHub API are:

- The "title" text (some READMEs do not have an H1 or H2 as the 1st heading)
- The number of internal links
- The number of external links
- The number of images, both `![]()` and `<img>`
- The number of images with alt text
- The count of H1, H2, and H3 elements
- Whether or not there is a Table of Contents or not

I also need the first elements that are text elements, ideally H1 followed by a paragraph followed by an H2, ignoring images. It would be hard to program that since I have seen other elements at the top of the repo, plus there are other issues. I am doing all of that manually.

I am also counting the number of code blocks which may or may not be useful. There are other metrics I am collecting that are subjective and would be difficult to add to a function.

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

## Acknowledgments

<!-- ✅ -->

Credit datasets, tutorials, or inspiration (maybe these)

- [5 tips for making your GitHub profile page accessible](https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/): The article that got me thinking about repo SEO
- [Awesome SEO tools](https://github.com/serpapi/awesome-seo-tools): decent list of tools
- [GitHub Search Engine Optimization (SEO): how to rank your repository in GitHub search](https://www.markepear.dev/blog/github-search-engine-optimization): Good article on specifics for GitHub Explore rank
- [GitHub SEO: Rank your repo and get adoption in 2026](https://nakora.ai/blog/github-seo): excellent tips
- [GitHub Pages SEO Analyzer](https://www.jekyllpad.com/tools/github-pages-seo-analyzer): Enter your GitHub page URL to get a report

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<br>

<!-- ## Resources

- List items here (Do I need this section?)

<br> -->

## Contributing

<!-- ✅ -->

Contributions are welcome! If you'd like to help improve this project, please read our [contribution guidelines](./CONTRIBUTING.md) on how to get started, our workflow, and code style expectations.

<!-- Should I add a stars button here like I've seen in other repos? -->

<br>

## License

<!-- ✅ -->

This project is licensed under the [MIT License](./LICENSE).

<div align="right">&#8673; <a href="#back-to-top">Back to Top</a></div>

<!--
📌 How to add a license:
  - https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/adding-a-license-to-a-repository
 -->

 <!-- 
 OTHER IMPORTANT LINKS

  📌 Accessible Markdown:
  - https://github.blog/developer-skills/github/5-tips-for-making-your-github-profile-page-accessible/

  📌 Create a PR Template:
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository
  - https://axolo.co/blog/p/part-3-github-pull-request-template
  - https://github.com/Kernix13/github-actions-dotfiles/blob/main/dotfiles.md#dot-github-folder

  📌 Create an issues template
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository
  - https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates

  ✅ Jupyter Markdown: 
  - https://www.ibm.com/docs/en/watson-studio-local/1.2.3?topic=notebooks-markdown-jupyter-cheatsheet
  - https://sqlbak.com/blog/wp-content/uploads/2020/12/Jupyter-Notebook-Markdown-Cheatsheet2.pdf
  - https://www.kaggle.com/code/cuecacuela/2025-the-ultimate-markdown-cheat-sheet

-->

<!--

1. ✅ SEO Title: 50-60 chars ideally, up to 70 is okay, 50-55 for mobile
2. ✅ SEO/Meta Description: 120-158 characters, closer to 120 for mobile
3. ✅ GitHub Explore Description: max 143 characters


NOTE: df = pd.read_csv('data/repo_metrics.csv', index_col='user_reponame')

python src/github_api.py

 ⭐⭐⭐ Every section/heading should earn its place
 -->

<!--

  DATA HEADINGS SUMMARY:
  - Data Sources - 29 ✅
  - Data Dictionary - 10 ✅
  - (Data) Visualizations ~ 8 ✅
  - Data Summary - 4
  - Data Cleaning + [others] ~ 4
  - Data Processing and Data Transformation - 3
  - Gathering the data - 3
  - Data Analysis - 2

  ✅ OTHER COMMON HEADINGS:
  - Project Summary/Summary - 3
  - Conclusion - 1
  - Research - 1

  - Project Challenges - 1
  - Streamlit - 1
  - Consider: bullet point Data Set summary with datatype counts
  - Features / Project Features - 4+ (is this Code:You capstone features?)

 -->
