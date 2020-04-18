from sql_alchemy import banco

class UserModel(banco.Model):
    __tablename__ = 'user_data'

    login = banco.Column(banco.String, primary_key=True)
    id = banco.Column(banco.String)
    node_id = banco.Column(banco.String)
    avatar_url = banco.Column(banco.String)
    gravatar_id = banco.Column(banco.String)
    url = banco.Column(banco.String)
    html_url = banco.Column(banco.String)
    followers_url = banco.Column(banco.String)
    following_url = banco.Column(banco.String)
    gists_url = banco.Column(banco.String)
    starred_url = banco.Column(banco.String)
    subscriptions_url = banco.Column(banco.String)
    organizations_url = banco.Column(banco.String)
    repos_url = banco.Column(banco.String)
    events_url = banco.Column(banco.String)
    received_events_url = banco.Column(banco.String)
    type = banco.Column(banco.String)
    site_admin = banco.Column(banco.String)
    name = banco.Column(banco.String)
    company = banco.Column(banco.String)
    blog = banco.Column(banco.String)
    location = banco.Column(banco.String)
    email = banco.Column(banco.String)
    hireable = banco.Column(banco.String)
    bio = banco.Column(banco.String)
    public_repos = banco.Column(banco.String)
    public_gists = banco.Column(banco.String)
    followers = banco.Column(banco.String)
    following = banco.Column(banco.String)
    created_at = banco.Column(banco.String)
    updated_at = banco.Column(banco.String)

    def __init__(self, user_data):
        for key in user_data:
            self.__dict__[key] = str(user_data[key])

    def json(self):
        dic = {}
        for key in sorted(self.__dict__.keys()):
            if key == '_sa_instance_state':
                pass
            else:
                dic[key] = str(self.__dict__[key])
        return dic

    @classmethod
    def find_user(cls, user_name):
        user = cls.query.filter(cls.login.ilike(user_name)).first()
        if user:
            return user
        return None

    def save_user(self):
        banco.session.add(self)
        banco.session.commit()


class RepoModel(banco.Model):
    __tablename__ = 'repos_data'

    id = banco.Column(banco.String, primary_key=True)
    node_id = banco.Column(banco.String)
    name = banco.Column(banco.String)
    full_name = banco.Column(banco.String)
    private = banco.Column(banco.String)
    owner = banco.Column(banco.String)
    html_url = banco.Column(banco.String)
    description = banco.Column(banco.String)
    fork = banco.Column(banco.String)
    url = banco.Column(banco.String)
    forks_url = banco.Column(banco.String)
    keys_url = banco.Column(banco.String)
    collaborators_url = banco.Column(banco.String)
    teams_url = banco.Column(banco.String)
    hooks_url = banco.Column(banco.String)
    issue_events_url = banco.Column(banco.String)
    events_url = banco.Column(banco.String)
    assignees_url = banco.Column(banco.String)
    branches_url = banco.Column(banco.String)
    tags_url = banco.Column(banco.String)
    blobs_url = banco.Column(banco.String)
    git_tags_url = banco.Column(banco.String)
    git_refs_url = banco.Column(banco.String)
    trees_url = banco.Column(banco.String)
    statuses_url = banco.Column(banco.String)
    languages_url = banco.Column(banco.String)
    stargazers_url = banco.Column(banco.String)
    contributors_url = banco.Column(banco.String)
    subscribers_url = banco.Column(banco.String)
    subscription_url = banco.Column(banco.String)
    commits_url = banco.Column(banco.String)
    git_commits_url = banco.Column(banco.String)
    comments_url = banco.Column(banco.String)
    issue_comment_url = banco.Column(banco.String)
    contents_url = banco.Column(banco.String)
    compare_url = banco.Column(banco.String)
    merges_url = banco.Column(banco.String)
    archive_url = banco.Column(banco.String)
    downloads_url = banco.Column(banco.String)
    issues_url = banco.Column(banco.String)
    pulls_url = banco.Column(banco.String)
    milestones_url = banco.Column(banco.String)
    notifications_url = banco.Column(banco.String)
    labels_url = banco.Column(banco.String)
    releases_url = banco.Column(banco.String)
    deployments_url = banco.Column(banco.String)
    created_at = banco.Column(banco.String)
    updated_at = banco.Column(banco.String)
    pushed_at = banco.Column(banco.String)
    git_url = banco.Column(banco.String)
    ssh_url = banco.Column(banco.String)
    clone_url = banco.Column(banco.String)
    svn_url = banco.Column(banco.String)
    homepage = banco.Column(banco.String)
    size = banco.Column(banco.String)
    stargazers_count = banco.Column(banco.String)
    watchers_count = banco.Column(banco.String)
    language = banco.Column(banco.String)
    has_issues = banco.Column(banco.String)
    has_projects = banco.Column(banco.String)
    has_downloads = banco.Column(banco.String)
    has_wiki = banco.Column(banco.String)
    has_pages = banco.Column(banco.String)
    forks_count = banco.Column(banco.String)
    mirror_url = banco.Column(banco.String)
    archived = banco.Column(banco.String)
    disabled = banco.Column(banco.String)
    open_issues_count = banco.Column(banco.String)
    license = banco.Column(banco.String)
    forks = banco.Column(banco.String)
    open_issues = banco.Column(banco.String)
    watchers = banco.Column(banco.String)
    default_branch = banco.Column(banco.String)
    temp_clone_token = banco.Column(banco.String)
    network_count = banco.Column(banco.String)
    subscribers_count = banco.Column(banco.String)

    def __init__(self, repo_data):
        for key in repo_data:
            if key == 'owner':
                self.__dict__[key] = str(repo_data[key]['login'])
            else:
                self.__dict__[key] = str(repo_data[key])

    def json(self):
        dic = {}
        for key in sorted(self.__dict__.keys()):
            if key == '_sa_instance_state':
                pass
            else:
                dic[key] = str(self.__dict__[key])
        return dic

    @classmethod
    def find_repo(cls, repo_name):
        repo = cls.query.filter(cls.owner.ilike(repo_name)).all()
        if repo:
            return repo
        return None

    def save_repo(self):
        banco.session.add(self)
        banco.session.commit()
