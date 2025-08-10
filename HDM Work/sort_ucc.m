%This program is to detect duplicates within an excel notebook, organizing data according to its  status.
%If status is empty, then replace with Done
ExampleTable=readtable('TASK - UCC Filing (1).xlsx')

%%
sorts={'DealName','UCCFiled'};
ExampleTable= sortrows(ExampleTable,sorts,'ascend')
vars= {'Funded','Yes', 'Done','TX'};
names= {'Stage','M2Paid','UCCFiled','CustomerState'};
ExampleTable= fillmissing(ExampleTable,'constant',vars,'DataVariables',names) 
%En esta sección se crea un string con los datos que se usarán para rellenar cuando exista un valor faltante.

%%

%En este bloque del código buscamos los valores únicos dentro de la tabla. Cuando se encuentran
% Se borran los valores repetidos, además ordenando la tabla para que no se pierda el orden ya creado
[mask1,ia]= unique(ExampleTable.DealName)
ExampleTable=ExampleTable(ia,:)
%%
%Y en esta sección buscamos que los deals que no sean de TX se eliminen
notTX= string(ExampleTable.CustomerState)
notTX= ~contains(notTX,'TX','IgnoreCase',true)
ExampleTable(notTX,:)= []
%%
writetable(ExampleTable,'UCC task 5-8-2025.xlsx')