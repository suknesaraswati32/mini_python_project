class message:
  message_counter=1
  def __init__(self,sender,content):
    self.sender=sender
    self.content=content
    self.id=message.message_counter
    message.message_counter+=1
    
    def __str__(self):
      return f"({self.id}){self.sender.username}:{self.content}"


class user:
  def __init__(self,username):
    self.username=username
    self.chatroom=None
    
    def join_chatroom(self,chatroom):
      if self.chatroom:
        print(f"{self.username} is already in a chatroom.")
      else:
        chatroom.add_user(self)
        self.chatroom=chatroom
        print(f"{self.username} joined the chatroom {chatroom.name}.")
    def leave_chatroom(self):
      if not self.chatroom:
        print(f"{self.username}is not in any chatroom")
      else:
        self.chatroom.remove_user(self)
        print(f"{self.username} left{self.chatroom.name}")
        self.chatroom=None
        
    def send_message(self,content):
      if not self.chatroom:
        print(f"{self.username} is not in any chatroom.") 
      else:
        self.chatroom.broadcast(self,content)
        
class chatroom:
  def __init__(self,name):
    self.name=name
    self.users=[]
    self.messages=[]
  def add_user(self,user):
    self.users.append(user)
  def remove_user(self,user):
    self.users.remove(user)
    
  def broadcast(self,sender,content):  
    message=message(sender,content)
    self.messages.append(message)
    print(message)
    
  def show_chat_history(self):
      print(f"Chat history for {self.name}:")
      for message in self.messages:
        print(message)
           
if __name__=="main__":
  room=chatroom("python Lounge")  
  
  u1=user("Alice")
  u2=user("Bob") 
  u3=user("Charlie")
  
  u1.join_chatroom(room)
  u2.join_chatroom(room)    
  
  u1.send_message("Hello everyone!")    
  u2.send_message("Hi Alice!")
  
  
  u3.join_chatroom(room)
  u3.send_message("Hey guys, what's up?")
  
  room.show_chat_history()
  
  u1.leave_chatroom()
  u2.leave_chatroom()
  u3.leave_chatroom()
  