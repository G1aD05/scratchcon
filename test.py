from scratchcon.actions import actions, login, conn, common

login.login("-g1ad0s-", "Glados")
conn.connect_project(1050221749)

actions.load()
actions.Project().post_comment("Hello")
