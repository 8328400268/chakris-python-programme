import matplotlib.pyplot as plt  
SPORTS = ['FOOTBALL', 'CRICKET', 'BADMINTON', 'BASKETBALL']  
slices = [7, 6, 5, 3] 
colors = ['y', 'r', 'g', 'b'] 
plt.pie(slices, labels = SPORTS, colors=colors,  
        startangle=90, shadow = True, explode = (0, 0, 0.1, 0), 
        radius = 1.2, autopct = '%1.1f%%') 
  
plt.legend() 
  

plt.show() 