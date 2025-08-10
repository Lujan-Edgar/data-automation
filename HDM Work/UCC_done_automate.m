%This script's goal is to automate the process of changing the status from "sent" to "Done" by 
%utilizing a .txt file that contains a list of deals
%First step is to import the information and save it on a string
% Leer contenido del archivo
Deal_names = fileread('ucc_lists.txt');
ExampleTable= readtable('UCC_FILING_FINAL.xlsx');
% Separar por líneas individuales
%strsplit permite crear strings dentro de un texto de forma que no entregue un bloque str por cada elemento
% en el archivo. Por ejemplo, en lugar de devolver {'J','u','a','n'}, strsplit devuelve {'Juan', ' ','Ga}.
Deal_list = strsplit(Deal_names,newline);
%%
%Esta sección es para cuando la lista contiene espacios
%En esta sección se busca crear un string a partir de las direccoines/nombres que aparecen en el documento
%Se va de 2 en 2 porque cada elemento par es un espacio y esos no nos interesan. 
blank_spaces=2:2:length(Deal_list);
Deal_list(blank_spaces)=[]; %Se eliminan los espacios en blanco de la lista Deal_list
%%
Deal_Name_Table= ExampleTable.DealName; %crer un array con los valores de la columna DealName
Deal_Name_Table= string(Deal_Name_Table); %convertir ese array en string
num_names=0; %contador
Deal_list = strtrim(Deal_list); %limpia espacios invisibles
%%
for i = 1:length(Deal_list)-1 %se resta uno porque el último valor es un espacio en blanco. %[output:group:37260520]
    idx = contains(Deal_Name_Table, Deal_list(i), 'IgnoreCase', true); 
    %Si alguno de los valores en la tabla coincide, entonces el índice nos indicará cuál es ese
    %ese valor que coincide con el valor i-esimo de Deal_list
    if any(idx)
        ExampleTable.UCCFiled(idx) = {'Done'};
        num_names = num_names + 1;
    else %En caso de que no se encuentre el valor, se imprimirá y podremos identificarlo
        %De esta forma evitamos saltarnos algún valor importante en la lista
        disp('No se encontró: ') %[output:4fce85fb] %[output:87f90681] %[output:0e4b8e3c] %[output:34b1dd41]
        disp(Deal_list(i)) %[output:9da133d3] %[output:50a9f1d5] %[output:912bf88e] %[output:3cb7cc72]
    end
end %[output:group:37260520]
if num_names == length(Deal_list)-1 %Busca que todos los elementos se hayan ubicado %[output:group:20b5ca58]
    disp('Todos los valores coincidieron')
    disp(num_names)
else
    disp('No todos las direcciones coincidieron') %[output:6ef59983]
end %[output:group:20b5ca58]
ExampleTable = sortrows(ExampleTable,'DealName','ascend');
%%
 writetable(ExampleTable,'DONE UCC TASK.xlsx') %Escribe una nueva tabla de Excel con los datos nuevos
 %Para usar estos datos, seleccionar toda la hoja, copiar y en el google sheet usar ctrl+shift+v 
 %esto pegará únicamente los valores y no alterará el formato de la hoja

%Se modificó el excel el 5/8/2025 a las 12:09
%modificar siempre después de su uso.

%[appendix]{"version":"1.0"}
%---
%[metadata:view]
%   data: {"layout":"onright"}
%---
%[output:4fce85fb]
%   data: {"dataType":"text","outputData":{"text":"No se encontró: \n","truncated":false}}
%---
%[output:9da133d3]
%   data: {"dataType":"text","outputData":{"text":"    'Irma Rodriguez The Preserve at Dyer Creek 1120 Preserve Pl'\n\n","truncated":false}}
%---
%[output:87f90681]
%   data: {"dataType":"text","outputData":{"text":"No se encontró: \n","truncated":false}}
%---
%[output:50a9f1d5]
%   data: {"dataType":"text","outputData":{"text":"    'Arash Debhdari 7370 Sleepy Ridge Cir'\n\n","truncated":false}}
%---
%[output:0e4b8e3c]
%   data: {"dataType":"text","outputData":{"text":"No se encontró: \n","truncated":false}}
%---
%[output:912bf88e]
%   data: {"dataType":"text","outputData":{"text":"    'Francisco J MartÃ­nez 103 Catalina Dr'\n\n","truncated":false}}
%---
%[output:34b1dd41]
%   data: {"dataType":"text","outputData":{"text":"No se encontró: \n","truncated":false}}
%---
%[output:3cb7cc72]
%   data: {"dataType":"text","outputData":{"text":"    'Navayakrishna Bandaru 611 Lily Ln'\n\n","truncated":false}}
%---
%[output:6ef59983]
%   data: {"dataType":"text","outputData":{"text":"No todos las direcciones coincidieron\n","truncated":false}}
%---
