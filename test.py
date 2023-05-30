from github import Github

# Provide your GitHub personal access token here
access_token = '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'

# Provide the organization name
organization_name = 'Systemlimited'

def get_user_push_time_config():
    # Create a PyGithub instance using the access token
    g = Github(access_token)

    try:
        # Get the organization
        org = g.get_organization(Systemlimited)
    

        # Get all projects in the organization
        projects = org.get_projects()

        for project in projects:
            print(f"Project: {project.name}")

            # Get all columns in the project
            columns = project.get_columns()

            for column in columns:
                print(f"\nColumn: {column.name}")

                # Get all cards in the column
                cards = column.get_cards()

                for card in cards:
                    if card.note:
                        note = card.note
                        if 'user: ' in note:
                            user_start_index = note.index('user: ') + len('user: ')
                            user_end_index = note.index('\n', user_start_index)
                            username = note[user_start_index:user_end_index]

                            if 'push_time: ' in note:
                                push_time_start_index = note.index('push_time: ') + len('push_time: ')
                                push_time_end_index = note.index('\n', push_time_start_index)
                                push_time_config = note[push_time_start_index:push_time_end_index]

                                print(f"User: {username}")
                                print(f"Push Time Configuration: {push_time_config}")
                                print("-" * 30)

    except Exception as e:
        print(f"Error retrieving push time configuration: {str(e)}")


# Run the app
get_user_push_time_config()
