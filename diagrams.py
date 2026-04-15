from graphviz import Digraph

# ---------- FIG 1: System Architecture ----------
def fig1():
    dot = Digraph(comment="FIG 1: System Architecture", format='png')
    
    dot.node('101', 'User')
    dot.node('102', 'SDK Layer')
    dot.node('103', 'QIR++ Compiler')
    dot.node('104', 'AI Optimization Engine')
    dot.node('105', 'Scheduler')
    dot.node('106', 'Execution Engine')
    dot.node('107', 'Quantum Hardware / Simulator')

    dot.edges([
        ('101','102'),
        ('102','103'),
        ('103','104'),
        ('104','105'),
        ('105','106'),
        ('106','107')
    ])

    dot.render('Fig1_System_Architecture', view=True)


# ---------- FIG 2: Hybrid Workflow ----------
def fig2():
    dot = Digraph(comment="FIG 2: Hybrid Workflow", format='png')

    dot.node('201', 'Classical Preprocessing')
    dot.node('202', 'Quantum Execution')
    dot.node('203', 'Classical Postprocessing')
    dot.node('204', 'AI Feedback Loop')

    dot.edges([
        ('201','202'),
        ('202','203'),
        ('203','204'),
        ('204','201')
    ])

    dot.render('Fig2_Hybrid_Workflow', view=True)


# ---------- FIG 3: Multi-Hardware ----------
def fig3():
    dot = Digraph(comment="FIG 3: Multi-Hardware", format='png')

    dot.node('301', 'Cloud A')
    dot.node('302', 'Cloud B')
    dot.node('303', 'Cloud C')
    dot.node('304', 'QuantumOS Core')
    dot.node('305', 'Quantum Hardware Backends')

    dot.edges([
        ('301','304'),
        ('302','304'),
        ('303','304'),
        ('304','305')
    ])

    dot.render('Fig3_Multi_Hardware', view=True)


# ---------- FIG 4: Internal Architecture ----------
def fig4():
    dot = Digraph(comment="FIG 4: Internal Architecture", format='png')

    dot.node('401', 'Multi-language SDK')
    dot.node('402', 'Parser')
    dot.node('403', 'QIR++ Generator')
    dot.node('404', 'AI Optimizer')
    dot.node('405', 'Scheduler')
    dot.node('406', 'Execution Manager')
    dot.node('407', 'Hardware Abstraction Layer')

    dot.edges([
        ('401','402'),
        ('402','403'),
        ('403','404'),
        ('404','405'),
        ('405','406'),
        ('406','407')
    ])

    dot.render('Fig4_Internal_Architecture', view=True)


# ---------- FIG 5: AI Optimization Loop ----------
def fig5():
    dot = Digraph(comment="FIG 5: AI Optimization Loop", format='png')

    dot.node('501', 'Execution Data')
    dot.node('502', 'AI Model Training')
    dot.node('503', 'Optimization Model')
    dot.node('504', 'Quantum Execution')

    dot.edges([
        ('501','502'),
        ('502','503'),
        ('503','504'),
        ('504','501')
    ])

    dot.render('Fig5_AI_Optimization', view=True)


# ---------- RUN ALL ----------
if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()