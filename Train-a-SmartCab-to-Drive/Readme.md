

n this project, we will work towards constructing an optimized Q-Learning driving agent that will navigate a Smartcab through its environment towards a goal. Since the Smartcab is expected to drive passengers from one location to another, the driving agent will be evaluated on two very important metrics: Safety and Reliability. A driving agent that gets the Smartcab to its destination while running red lights or narrowly avoiding accidents would be considered unsafe. Similarly, a driving agent that frequently fails to reach the destination in time would be considered unreliable. Maximizing the driving agent's safety and reliability would ensure that Smartcabs have a permanent place in the transportation industry.


Safety and Reliability are measured using a letter-grade system as follows:


  Grade 	                      Safety 	                                                        Reliability
  
   A+ 	        Agent commits no traffic violations,                              Agent reaches the destination in time 
               and always chooses the correct action. 	                                    for 100% of trips.

   A 	      Agent commits few minor traffic violations,                           Agent reaches the destination on time
             such as failing to move on a green light. 	                                for at least 90% of trips.

   B 	      Agent commits frequent minor traffic violations,                      Agent reaches the destination on time
              such as failing to move on a green light. 	                              for at least 80% of trips.

   C 	      Agent commits at least one major traffic violation,                   Agent reaches the destination on time
                such as driving through a red light. 	                                  for at least 70% of trips.

   D 	          Agent causes at least one minor accident,                         Agent reaches the destination on time
            such as turning left on green with oncoming traffic. 	                      for at least 60% of trips.

   F 	          Agent causes at least one major accident,                       Agent fails to reach the destination on time
            such as driving through a red light with cross-traffic. 	                  for at least 60% of trips.
