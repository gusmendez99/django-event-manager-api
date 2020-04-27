from parents.models import Parent
from babies.models import Baby  
from events.models import Event
from django.utils.timezone import now

from django.contrib.auth.models import User

#Users
User.objects.create_superuser('julio', 'julio@gmail.com', 'julio1234')
User.objects.create_superuser('mario', 'mario@gmail.com', 'mario1234')

#Parents
julhs = Parent()
julhs.username = "julio"
julhs.first_name = "Julio"      
julhs.last_name = "Hernandez"   
julhs.age = 25    
julhs.save()      
      
mario = Parent()
julhs.username = "mario"
mario.first_name = "Mario" 
mario.last_name = "Gomez" 
mario.age = 40
mario.save()

#Babies
maria = Baby()
maria.first_name = "Maria"
maria.last_name = "Gomez"      
maria.age = 1
maria.parent = mario
maria.save()

lupita = Baby()  
lupita.first_name = "Lupita"   
lupita.last_name = "Gomez"     
lupita.age = 1   
lupita.parent = mario   
lupita.save() 

rosa = Baby()    
rosa.first_name = "Rosa"
rosa.last_name = "Hernandez"   
rosa.age = 2     
rosa.parent = julhs     
rosa.save()      

fernando = Baby()
fernando.first_name = "Fernando"      
fernando.last_name = "Hernandez"      
fernando.age = 1 
fernando.parent = julhs 
fernando.save()  


#Events
  
event1 = Event(type="poop", datetime=now(), description = "Poop a lot",baby=fernando)
event1.save()    

event2 = Event(type="eat", datetime=now(), description = "Eat a lot", baby=lupita)
event2.save()    

event3 = Event(type="pee", datetime=now(), description = "Pee a lot", baby=maria)
event3.save()    

event4 = Event(type="poop", datetime=now(), description = "Poop a lot", baby=maria)
event4.save()    