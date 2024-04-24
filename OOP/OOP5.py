class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comment(first,second):
        return f"{first} {second}"

my_comment = Comment("My comment")

n_1 = Comment.merge_comments("Привет,","студент!")
print(n_1)
n_2 = Comment.merge_comments("Great","OK")
print(n_2)