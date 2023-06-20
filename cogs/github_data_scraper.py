from discord.ext import commands
from utils.api import GithubAPI
from utils.db import SupabaseInterface
import markdown, re


def markdownParser(markdown_content):

    #Taking metadata
    markdown_metadata = markdown_content.split('---')[1]

    # Parse Markdown to HTML
    html = markdown.markdown(markdown_metadata)
    print("-------METADATA----------")

    # Split HTML into sections using heading tags as delimiters
    sections = re.split("</h3>|<h3>", html)
    while '' in sections:
        sections.remove('')
    print("------SECTIONS---------")
    for section in sections:
        print(sections, section)
        section.strip()
        section = re.split("<p>|</p>", section)
    # Define regex pattern to match '\n', ':', and any html tags'<>'
        pattern = re.compile(r'[\n]|[:]|<(.*?)>')

    # Remove matching substrings from each string
    clean_sections = [re.sub(pattern, '', s) for s in sections]
    for section in clean_sections:
        print('---')
        print(section)

    # Initialize dictionary
    markdown_dict = {}
    for i in range(0,len(clean_sections), 2):
        print('i',i)
        markdown_dict[clean_sections[i]] = clean_sections[i+1]
    print(markdown_dict)
    return markdown_dict


class GithubDataScraper(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    

    @commands.command()
    async def update_prs(self, ctx):
        return 
    
    @commands.command()
    async def update_issues(self, ctx): 
        return
    
    @commands.command()
    async def update_commits(self, ctx):
        return 
    
    @commands.command()
    async def add_issue(self, ctx):
        repo = 'Code4GovTech/C4GT'
        number = '12'
        client = GithubAPI('https://github.com/Code4GovTech/C4GT/issues/12')
        issue = client.get_issue(repo, number)
        markdown_contents = markdownParser(issue["body"])
        issue_data = {
            "name":issue["title"],     #name of ticket
            "product":issue["repository_url"].split('/')[-1],
            "complexity":markdown_contents["Complexity"],
            "project_category":markdown_contents["Category"].split(','),
            "project_sub_category":markdown_contents["Sub Category"].split(','),
            "reqd_skills":markdown_contents["Tech Skills Needed"]

        }

        supabase = SupabaseInterface("ccbp_tickets")
        supabase.insert(issue_data)


    

    
    




async def setup(bot):
    await bot.add_cog(GithubDataScraper(bot))