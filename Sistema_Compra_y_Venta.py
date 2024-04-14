car_dni_ruc=["0","1","2","3","4","5","6","7","8","9"]

car_doc=["-", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
         "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
         "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

car_nom=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
         "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

prod_stk={"Aceite":14,"Leche":30,"Azúcar":45,"Arroz":56,"Atún":60,
          "Colores":45,"Lápiz":67,"Temperas":79,
          "Detergente":80,"Lejía":67,"Lava-vajilla":50,"Desinfectante":48}

prod_pre_cmp={"Aceite":3.50,"Leche":1.20,"Azúcar":6.50,"Arroz":2.50,"Atún":3.50,
              "Colores":5.00,"Lápiz":3.00,"Temperas":4.00,
              "Detergente":1.00,"Lejía":4.00,"Lava-vajilla":4.00,"Desinfectante":5.30}

prod_pre_ven={"Aceite":5.50,"Leche":3.20,"Azúcar":9.50,"Arroz":2.50,"Atún":4.50,
              "Colores":7.00,"Lápiz":5.00,"Temperas":6.00,
              "Detergente":2.00,"Lejía":6.00,"Lava-vajilla":6.00,"Desinfectante":7.30}


dni_nom={}
l_vt=[]
c_v=0
c=1

ruc_nom={}
l_cm=[]
c_c=0

mn_p=0
print('\n       Tienda "Ahorra-Express"\n'  )
while mn_p!=5:
    print("\n         Menu Principal\n")
    print("="*35)
    print("1.- Realizar una compra")
    print("2.- Realizar una Venta")
    print("3.- Actualización de Productos")
    print("4.- Reportes")
    print("5.- Salir")
    print("="*35)


    #cuadro de productos
    cd_vt=f"""\n
╓-----------------------------------------------------------------------------------╖
║                          Cuadro de Productos(Venta)                               ║
╟-----------------------------------------------------------------------------------╢
          Abarrotes        ┃    Útiles Escolares     ┃           Limpieza            
╟-----------------------------------------------------------------------------------╢
    Producto  ┃    Precio   ┃  Producto  ┃   Precio   ┃   Producto    ┃    Precio       
╟-----------------------------------------------------------------------------------╢ 
    Aceite    ┃  S/. {prod_pre_ven['Aceite']:>5.2f}  ┃  Colores   ┃  S/. {prod_pre_ven['Colores']:>5.2f} ┃ Detergente    ┃  S/. {prod_pre_ven['Detergente']:>5.2f}  
    Leche     ┃  S/. {prod_pre_ven['Leche']:>5.2f}  ┃  Lápiz     ┃  S/. {prod_pre_ven['Lápiz']:>5.2f} ┃ Lejía         ┃  S/. {prod_pre_ven['Lejía']:>5.2f}  
    Azúcar    ┃  S/. {prod_pre_ven['Azúcar']:>5.2f}  ┃  Temperas  ┃  S/. {prod_pre_ven['Temperas']:>5.2f} ┃ Lava-vajilla  ┃  S/. {prod_pre_ven['Lava-vajilla']:>5.2f}  
    Arroz     ┃  S/. {prod_pre_ven['Arroz']:>5.2f}  ┃            ┃            ┃ Desinfectante ┃  S/. {prod_pre_ven['Desinfectante']:>5.2f}  
    Atún      ┃  S/. {prod_pre_ven['Atún']:>5.2f}  ┃            ┃            ┃               ┃             
╙-----------------------------------------------------------------------------------╜\n
    """
    ####################

    
    while True:
        try:
            mn_p=int(input("Ingrese Opción<1-5>: "))
            if mn_p<0 or mn_p>5:
                print("\n'ERROR' Opción fuera del Rango<1-5>\n")
            else:
                break
        except ValueError:
            print("\n'ERROR' Valor no admitido\n")
    if mn_p==1:
        while True:
            dt_cmd=[]            
            cn=0
            dt_cm=[]
            n_do=input("Ingrese su N. de Documento: ")
            if any(n_d not in car_doc for n_d in n_do):  # validamos que solo se utilizen valores alfanumericos
                print("\n'ERROR' Algunos caracteres no están permitidos\n")
            elif len(n_do) != 14:  # Validamos que se tenga los digitos adecuados
                print("\n'ERROR' Debe tener 2 guiones y 12 caracteres\nEjemplo ==> aaaa-aaaa-aaaa\n")
            elif any("-" not in n_do for n_do in n_do[4]) or any(
                     "-" not in n_do for n_do in n_do[9]):  # Validamos que el guion se encuentre en el lugar adecuado
                print("\n'ERROR' Número de cuenta erroneo\nEjemplo ==> aaaa-aaaa-aaaa\n")
            else:
                break
        while True:
            n_ruc=input("Ingrese su RUC: ")
            if n_ruc in ruc_nom:
                print(f"Nombre: {ruc_nom[n_ruc]}")
                dt_cmd.append(n_ruc)
                dt_cm.append(n_do)
                break
            elif any(n_r not in car_dni_ruc for n_r in n_ruc):
                print("\n'ERROR' Algunos caracteres no están permitidos\n")
            elif len(n_ruc)!= 11:
                print("\n'ERROR' Cantidad de digitos fuera de lo establecido(11 Digitos)\n")
            elif n_ruc not in ruc_nom:
                print("\nRUC no encontrado\n\nIniciando Registro:\n")
                while True:
                    n_ruc=input("Ingrese su RUC: ")
                    if n_ruc in ruc_nom:
                        print("\n'ERROR' Número de RUC ya ingresado\n")
                    elif any(n_r not in car_dni_ruc for n_r in n_ruc):
                        print("\n'ERROR' Algunos caracteres no están permitidos\n")
                    elif len(n_ruc)!= 11:
                        print("\n'ERROR' Cantidad de digitos fuera de lo establecido(11 Digitos)\n")
                    else:
                        break
                while True:
                    nom_pro = input("Ingrese su nombre: ")
                    if any(nm_pv not in car_nom for nm_pv in nom_pro):
                        print("\n'ERROR' Algunos caracteres no están permitidos\n")
                    else:
                        break
                ruc_nom.update({n_ruc:nom_pro})
                print("\nRegistro Exitoso\n")        
        while True:
            com=input("Boleta o factura: ").upper()
            if com!="BOLETA" and com!="FACTURA":
                print("\n'ERROR' Por favor ingrese el tipo correcto de comprobante (Boleta o Factura)\n")
            else:
                dt_cm.append(com)
                break
        c_pr=[]
        print(f"""\n
╓-----------------------------------------------------------------------------------╖
║                          Cuadro de Productos(Compra)                              ║
╟-----------------------------------------------------------------------------------╢
          Abarrotes        ┃    Útiles Escolares     ┃           Limpieza           
╟-----------------------------------------------------------------------------------╢
   Producto  ┃    Precio   ┃  Producto  ┃   Precio   ┃   Producto    ┃    Precio       
╟-----------------------------------------------------------------------------------╢
    Aceite    ┃  S/. {prod_pre_cmp['Aceite']:>5.2f}  ┃  Colores   ┃  S/. {prod_pre_cmp['Colores']:>5.2f} ┃ Detergente    ┃  S/. {prod_pre_cmp['Detergente']:>5.2f}  
    Leche     ┃  S/. {prod_pre_cmp['Leche']:>5.2f}  ┃  Lápiz     ┃  S/. {prod_pre_cmp['Lápiz']:>5.2f} ┃ Lejía         ┃  S/. {prod_pre_cmp['Lejía']:>5.2f}  
    Azúcar    ┃  S/. {prod_pre_cmp['Azúcar']:>5.2f}  ┃  Temperas  ┃  S/. {prod_pre_cmp['Temperas']:>5.2f} ┃ Lava-vajilla  ┃  S/. {prod_pre_cmp['Lava-vajilla']:>5.2f}  
    Arroz     ┃  S/. {prod_pre_cmp['Arroz']:>5.2f}  ┃            ┃            ┃ Desinfectante ┃  S/. {prod_pre_cmp['Desinfectante']:>5.2f}  
    Atún      ┃  S/. {prod_pre_cmp['Atún']:>5.2f}  ┃            ┃            ┃               ┃             
╙-----------------------------------------------------------------------------------╜\n
""")
        while True: 
            prd = input("Producto a Comprar: ").capitalize()
            if prd not in prod_stk:
                print("\n'ERROR' Producto no encontrado o valor no admitido\n")
            else:
                break
        while True:
            try:
                can=int(input("Ingrese Cantidad: "))
                if can<=0:
                    print("\n'ERROR' Cantidad Nula o Negativa\n")
                else:
                    print(f"Precio        :S/. {prod_pre_cmp[prd]:>6.2f}")
                    print(f"Total a Pagar :S/. {(prod_pre_cmp[prd]*can):>6.2f}\n")
                    c_pr.append(prd)
                    c_pr.append(can)
                    c_pr.append(prod_pre_cmp[prd]*can)                    
                    break              
            except ValueError:
                print("\n'ERROR' Valor no admitido\n")        
        dt_cm.append(c_pr)
        dt_cmd.append(dt_cm)
        l_cm.append(dt_cmd)
        for b in range(len(l_cm)):
            if n_ruc==l_cm[b][0]:
                if len(l_cm[b][1])==3:
                    l_cm[b][1].append(prod_pre_cmp[prd]*can)
                else:
                    l_cm[b][1][3]=l_cm[b][1][3]+(prod_pre_cmp[prd]*can)
                break
        prod_stk[prd]=prod_stk[prd]+can
        c_c=1
    elif mn_p==2:
        print(f"\nNúmero de Documento: B-{c}")
        while True:
            dt_vt=[]
            dt_pr=[]
            dni=input("Ingrese su DNI: ")
            if dni in dni_nom:
                print(f"Nombre: {dni_nom[dni]}\n")
                dt_vt.append(dni)
                break
            elif any(x not in car_dni_ruc for x in dni):
                print("\n'ERROR' Algunos caracteres no estan permitidos\n")
            elif len(dni)!=8:
                print("\n'ERROR' Cantidad de digitos fuera de lo establecido(8 Digitos)\n")
            elif dni not in dni_nom:
                print("\nDNI no encontrado\n\nIniciando Registro:\n")
                while True:
                    dni=input("Ingrese su DNI: ")
                    if dni in dni_nom:
                        print("\n'ERROR' Número de DNI ya ingresado")
                    elif any(x not in car_dni_ruc for x in dni):
                        print("\n'ERROR' Algunos caracteres no estan permitidos\n")
                    elif len(dni)!=8:
                        print("\n'ERROR' Cantidad de digitos fuera de lo establecido(8 Digitos)\n")
                    else:
                        break
                while True:
                    nom=input("Ingrese su Nombre: ")
                    if any(n not in car_nom for n in nom):
                        print("\n'ERROR' Algunos caracteres no estan permitidos\n")
                    else:
                        break
                dni_nom.update({dni:nom})
                print("\nRegistro realizado\n")
        op="SI"
        pro=[]
        t=0
        print(cd_vt)
        while op!="NO":
            while True:
                pr=input("Producto: ").capitalize()
                if pr not in prod_pre_ven:
                    print("\n'ERROR' Producto no encontrado\n")
                else:
                    break
            while True:
                try:
                    ct=int(input("Cantidad: "))
                    if ct>(prod_stk[pr]):
                        print("\n'ERROR' No existe suficiente Stock")
                    elif ct<1:
                        print("\n'ERROR' Cantidad negativa o nula")
                    else:
                        print(f"Precio: {prod_pre_ven[pr]}\n")
                        i=prod_pre_ven[pr]*ct
                        pro.append(pr)
                        pro.append(ct)
                        pro.append(f"{prod_pre_ven[pr]:.2f}")
                        pro.append(f"{i:.2f}")
                        t=t+i
                        break
                except ValueError:
                    print("Valor no admitido")
            prod_stk[pr]=prod_stk[pr]-ct        
            while True:
                op=input("Desea seguir comprando<SI-NO>: ").upper()
                if op!="SI" and op!="NO":
                    print("\n'ERROR' Por favor ingresar 'SI' o 'NO'\n")
                else:
                    break
        dt_pr.append(f"B-{c}")
        dt_pr.append(pro)
        dt_pr.append(f"{t:.2f}")
        dt_vt.append(dt_pr)
        l_vt.append(dt_vt)
        print(f"""
 DNI     : {dni}                        Num_Doc: B-{c}
 Nombre  : {dni_nom[dni]}\
        """)
        print("""\
╔══════════════════╦══════════╦═══════════╦═══════════════╗
║ Producto         ║Precio    ║Cantidad   ║SubTotal       ║""")
        for z in range(0,(len(pro)),+4):
            print(f"""\
╠══════════════════╬══════════╬═══════════╬═══════════════╣
║ {pro[z]:<17}║S/. {pro[z+2]:>6}║{pro[z+1]:>6}     ║S/. {pro[z+3]:>11}║\
""")
        print("""\
╚══════════════════╩══════════╩═══════════╬═══════════════╣\
""")
        print(f"""\
                                Total     ║S/.  {t:>10.2f}║
                                          ╚═══════════════╝\
""")
        c_v=1
        c=c+1
    elif mn_p==3:
        print(cd_vt)
        while True:
            ac_pre=input("Nombre del producto a actualizar: ").capitalize()
            if ac_pre not in prod_pre_ven:
                print("\n'ERROR' Producto no encontrado\n")
            else:
                break
        while True:
            nu_pre=float(input("Ingrese el nuevo precio:"))
            if nu_pre<1:
                print("\n'ERROR' Nuevo precio negativo o nulo\n")
            else:
                prod_pre_ven[ac_pre]=nu_pre
                print("\nPrecio del producto actualizado\n")
                break        
    elif mn_p==4:
        mn_r=0
        while mn_r!=5:
            print("\n        Menú de Reportes\n")
            print("="*45)
            print("1.- Listado de Productos - Precio")
            print("2.- Listado de Productos - Stock")
            print("3.- Consulta de Ventas por Cliente")
            print("4.- Consulta de Compras por Proveedor")
            print("5.- Regresar al Menú Principal")
            print("="*45)
            while True:
                try:
                    mn_r=int(input("Ingrese Opción<1-5>: "))
                    if mn_r<0 or mn_r>5:
                        print("\n'ERROR' Opción fuera del Rango<1-5>\n")
                    else:
                        break
                except ValueError:
                    print("\n'ERROR' Valor no admitido\n")
            if mn_r==1:
                print()
                for p_p_v in prod_pre_ven.keys():
                    print(f"Producto ==> {p_p_v:<14} ---> S/. {prod_pre_ven[p_p_v]:.2f}")
            elif mn_r==2:
                print()
                for p_s in prod_stk.keys():
                    print(f"Producto ==> {p_s:<14} ---> {prod_stk[p_s]:>5} Unidades")
            elif mn_r==3:
                if c_v==0:
                    print("\nNo se encuentran clientes registrados\n")
                else:
                    b_dni=input("\nIngresar DNI: ")
                    if b_dni in dni_nom:
                         print(f"\nNombre   : {dni_nom[b_dni]}")
                         print(f"DNI      : {b_dni}")
                         for b in range(len(l_vt)): 
                              if b_dni==l_vt[b][0]:
                                   print(f"Num_Doc  : {l_vt[b][1][0]}")
                                   print("-"*55)
                                   print(" Producto          Precio     Cantidad   SubTotal ")
                                   print("-"*55)
                                   for o in range(0,(len(l_vt[b][1][1])),+4):
                                       print(f" {l_vt[b][1][1][o]:<14}{l_vt[b][1][1][o+1]:>9}{l_vt[b][1][1][o+2]:>11}{l_vt[b][1][1][o+3]:>13}")     
                                   print("-"*55) 
                                   print(f"Total S/. : {l_vt[b][1][2]:>36}\n")
                    else:
                        print("\n'ERROR' DNI no encontrado\n")
            elif mn_r==4:
                if c_c==0:
                    print("\nNo se encuentran proveedores registrados\n")
                else:
                    b_ruc=input("Ingrese el RUC del Proveedor: ")
                    if b_ruc in ruc_nom:
                        print(f"\nNombre : {ruc_nom[b_ruc]}")
                        print(f"RUC      : {b_ruc}")
                        for z in range(len(l_cm)):
                            if b_ruc==l_cm[z][0]:
                                if l_cm[z][1][1]=="BOLETA":
                                    print(f"""\
╓======================================================╖

                  Ahorra-Express
                  
 N° DOC : {l_cm[z][1][0]:<16}{l_cm[z][1][1]:>25}
 RUC    : {b_ruc}
 Nombre : {ruc_nom[b_ruc]}
 ------------------------------------------------------
  Producto         Cantidad    Precio    Total a Pagar
 ------------------------------------------------------
  {l_cm[z][1][2][0]:<15}{l_cm[z][1][2][1]:>9}     {prod_pre_cmp[l_cm[z][1][2][0]]:>6.2f}        {l_cm[z][1][2][2]:>9.2f}


 ------------------------------------------------------
                                     Total   {l_cm[z][1][2][2]:>9.2f}

╙======================================================╜\
 """)
                                elif l_cm[z][1][1]=="FACTURA":
                                    print(f"""\
╒════════════════════════════════════════════════════════════════════════════════╕
│                                                                                │
│ Ahorra-Express                                               {l_cm[z][1][1]:>13}     │
│                                                                                │
│N° DOC : {l_cm[z][1][0]:<16}                                     RUC: {b_ruc}  │
│Nombre: {ruc_nom[b_ruc]:<72}│
╞══════════╤══════════════════════════════════════════╤══════════╤═══════════════╡
│ Cantidad │ Producto                                 │  Precio  │ Total a Pagar │
╞══════════╪══════════════════════════════════════════╪══════════╪═══════════════╡
│    {l_cm[z][1][2][1]:<4}  │ {l_cm[z][1][2][0]:<41}│ {prod_pre_cmp[l_cm[z][1][2][0]]:>7.2f}  │ {l_cm[z][1][2][2]:>13.2f} │
╞══════════╪══════════════════════════════════════════╪══════════╪═══════════════╡                            
│          │                                          │          │               │
╞══════════╪══════════════════════════════════════════╪══════════╪═══════════════╡
│          │                                          │          │               │
╘══════════╧══════════════════════════════════════════╧══════════╪═══════════════╡
                                                          Total  │ S/. {l_cm[z][1][2][2]:>9.2f} │
                                                                 ╘═══════════════╛\
""")
                        print(f"\nTotal de todas las compras: S/. {l_cm[z][1][3]:.2f}\n")
                    else:
                        print("\n'ERROR' RUC no encontrado\n")


print()
print("="*32)
print("GRACIAS POR TODO - VUELVA PRONTO")
print("="*32)
input(" ")                    

        

        





























    
