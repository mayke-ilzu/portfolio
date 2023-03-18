# Ford GoBike / Bay Wheels - Exploratory Analysis

Bay Wheels, previously Ford GoBike, is a regional public bicycle sharing system in California's San Francisco Bay Area. It is operated by Motivate in a partnership with the Metropolitan Transportation Commission and the Bay Area Air Quality Management District. Bay Wheels is 'the first regional and large-scale bicycle sharing system deployed in California and on the West Coast of the United States. It was established as Bay Area Bike Share in August 2013. As of January 2018, the Bay Wheels system had over 2,600 bicycles in 262 stations across San Francisco, East Bay and San Jose.

In June 2017 the system was officially re-launched as Ford GoBike in a partnership with Ford Motor Company. After Motivate's acquisition by Lyft, the system was renamed to Bay Wheels in June 2019. The system is expected to expand to 7,000 bicycles around 540 stations in San Francisco, Oakland, Berkeley, Emeryville, and San Jose.

This document explore a data set includes information about individual rides made in Bay Wheels covering the greater San Francisco Bay area.


## Investigation Overview

In this analysis I wanted to understand the profile and behavior of Bay Wheels users, which is a regional public bicycle sharing system. For this, I focused on the understanding of: user type, gender and day of week that the service was used. Some features served as support to understand the aforementioned focus, such as: trip duration, user age and trip start and end hour.


## Dataset Overview

The data consisted of 183412 trip records, containing features that can be divided into three types of information: Route, Location and Customers.

## Conclusions

After analyzing the data, the main insights were identified:
- Most bike sharing lasted up to 10 minutes, with the greatest mass being between 5 and 10 minutes
- Most users are subscribed, meaning there are few occasional customers
- We can identify 2 peak times for bike sharing start hour: from 8 am to 9 am and 5 pm to 6 pm. As most users are subscribers, they may have greater influence on peak hours, which are exactly business hours where people usually go to work, so this may be a behavior of these users and the greater distribution of trips on weekdays can reinforce this hypothesis
- End hour distribution is practically the same as start hour, which makes sense as bike sharing usually lasts an average of 9 minutes
- Market St and San Francisco Caltrain Station 2 are the most embarking and disembarking stations
- Although more males use the service this may not be a particularity of service users, since we do not know the gender distribution in the city
- Users who are occasional customers have a longer trip duration. This makes sense, as subscribers should use the bike more routinely and for a specific purpose (like go to work), while occasional customers should use it more for leisure or longer trips
- The trip duration is practically the same for all genders
- The age and trip duration is practically the same for all genders
- Contrary to what I imagined, peak times are very similar between user types, but we can see an interesting behavior: excluding peak times, subscribers tend to use the service more at afternoon than occasional customers, who use more at evening.
- Contrary to what is seen in the behavior of subscribers, the use of the service by occasional customers remains at the same level on weekends
- Analysing the relationship between usuer type, start hour and start day of week we confirm that the peak hours of usage during the week is practically the same for both user types. However, the difference between the user types on the weekend is much more evident: occasional customers use the service more, especially between 10am and 5pm. This reinforces the idea that these customers are the ones who use the service more for leisure
- Although subscribers have a smaller number of users on weekends, this is not reflected in the average trip duration behavior: on weekends for both user types the average trip duration is longer on weekend
- Even though it's a small difference, for both user types we noticed a drop in the average age during the weekends. This difference is more noticeable for occasional customers, what tells us that younger people use the service occasionally for leisure at weekend

Given these insights, what was taken for an explanatory analysis was the difference in behavior between subscribers and occasional customers. Mainly, the different behavior during the weekends.

## References

- Udacity material
- [Matplotlib colors list](https://matplotlib.org/stable/gallery/color/named_colors.html)
- [Set differente color for barplot](https://stackoverflow.com/questions/31074758/how-to-set-a-different-color-to-the-largest-bar-in-a-seaborn-barplot)
- [Plot categorical data](http://seaborn.pydata.org/tutorial/categorical.html?highlight=bar%20plot)
- [Pie chart](https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f)
- [Sort categorial data](https://soulsinporto.medium.com/custom-sort-a-pandas-dataframe-with-pd-categorical-c4eec8343957)