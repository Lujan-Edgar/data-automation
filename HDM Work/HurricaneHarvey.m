%% Analyzing hurricane harvey's Impact
% In this livescript my goal will be to analyze the damages caused by the hurrican 
% harvey during the months of august and september. This is the final project 
% of the matlab course and here, I plan to use all the tools that have been provided 
% to me to showcase my abilities as a new data analyst.

%Lets expport the csv file with a special function that contains only the
%values we will be needing to work.
Harvey=StormEvents("StormEvents_2017_finalProject.csv");
targetStates = {'ARKANSAS','KENTUCKY','LOUISIANA','MISSISSIPPI','NORTH CAROLINA','TENNESSEE','TEXAS'};
Harvey = Harvey(ismember(Harvey.State,targetStates) | ismissing(Harvey.State),:)
%%
Harvey = Harvey(ismember(Harvey.Month,{'August','September'}) | ismissing(Harvey.Month),:);
Harvey = sortrows(Harvey, "Month", "descend");
%After selecting the desired months, lets select the specified dates that
%we will be using for our analysis.
Harvey = Harvey(Harvey.Begin_Date_Time >= '2017-08-17 19:14:00' & Harvey.Begin_Date_Time < '2017-09-03 12:00:01' | ismissing(Harvey.Begin_Date_Time),:);
Harvey = Harvey(Harvey.End_Date_Time >= '2017-08-17 20:30:00' & Harvey.End_Date_Time < '2017-09-03 23:59:01' | ismissing(Harvey.End_Date_Time),:);
Harvey = sortrows(Harvey, "Begin_Date_Time");
Harvey = sortrows(Harvey, "End_Date_Time")
%%
%Now that I've selected the specific months and days of the month that I
%will be using to explore the data.
Harvey = Harvey(~ismissing(Harvey.Crop_Cost),:);
Harvey = sortrows(Harvey, "Property_Cost", "descend");
Harvey = sortrows(Harvey, "Crop_Cost", "descend")
%Here we will be looking after the State that suffered from the most
%damages
Harvey.Total_Cost= Harvey.Property_Cost + Harvey.Crop_Cost;
Damages= groupsummary(Harvey,"State","max","Total_Cost");
Damages = sortrows(Damages, "max_Total_Cost", "descend")
%%
%In this section we will be looking at the damage per county
State= 'ARKANSAS'; %this button allows you to look at each State individually.
idx= Harvey.State == State;
County_Damages= Harvey(idx,:);
County_Damages = sortrows(County_Damages, "CZ_Name")
%Now that we've separated by state and county, lets focus on the number of
%events that took place in each county and the total cost.

Damage_individual= groupsummary(County_Damages,"CZ_Name",'sum','Total_Cost');
Damage_individual = sortrows(Damage_individual, "sum_Total_Cost", "descend")
%In this last section we will be just counting the number of events that
%took place in each county, looking at each one individually.
Frequent_Event= groupsummary(County_Damages,"CZ_Name",'mode','Event_Type');
Frequent_Event = sortrows(Frequent_Event, "mode_Event_Type");
Frequent_Event = sortrows(Frequent_Event, "GroupCount", "descend")
%Finally, to end this whole thing, lets look at the most ocurrent event
%throughout Harvey's path.
Most_Ocurrent= groupsummary(Harvey,'State','mode', 'Event_Type');

Most_Ocurrent = sortrows(Most_Ocurrent, "GroupCount", "descend")