    ###### Symbolic Mathematics ######

        ## Define symbols ##
        # x, y = sp.symbols('x y')
        # t = sp.symbols('t', real=True)
        
        ## Define functions ##
        # f = sp.cos(x) * sp.exp(-y)
        # g = sp.sin(x) * sp.sqrt(-y**2 + 1)

        ## Calculate derivatives ##
        # df_dx = sp.diff(f, x)
        # dg_dy = sp.diff(g, y)

        ## Evaluate functions at specific points ##
        # eval_f = f.subs({x: sp.pi/4, y: 0}).evalf()
        # eval_g = g.subs({x: sp.pi/4, y: 0}).evalf()

        # pprint(f)
        # pprint(g)
        # pprint(df_dx)
        # pprint(dg_dy)   

        ## Result:
        # cos(x)*exp(-y)
        # sqrt(-y**2 + 1)*sin(x)
        # -sin(x)*exp(-y)
        # -y*sin(x)/sqrt(-y**2 + 1)
        # 0.707106781186548
        # 0.707106781186548

    ###### Unit Calculations ######

        ## Calculations with units
        # r1 = 120 * ohm
        # r2 = 665 * ohm
        # r3 = 120 * ohm

        ## Define voltage source
        # vs = 5 * V

        ## Calculate equivalent resistance of r2 and r3 in parallel
        # Rp = (r2 * r3) / (r2 + r3)

        ## Calculate total current using Ohm's Law
        # iT = vs / (r1 + Rp)

        # print(f"Current i: {iT}")

        ## Result:
        # Current i: 0.0200000000000000 A
