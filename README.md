# design_patterns
大话设计模式python实现

simple_factory_pattern.py
简单工厂模式(Simple Factory Pattern):是通过专门定义一个类来负责创建其他类的实例，被创建的实例通常都具有共同的父类.

strategy_pattern.py
策略模式(Strategy Pattern):它定义了算法家族,分别封装起来,让他们之间可以相互替换,此模式让算法的变化,不会影响到使用算法的客户.

decorator_pattern.py
装饰模式(Decorator Pattern):动态的给一个对象添加一些额外的职责,就增加功能来说,装饰模式比生成子类更为灵活.

proxy_pattern.py
代理模式(Proxy Pattern):为其他对象提供一种代理以控制对这个对象的访问.

factory_method_pattern.py
工厂方法模式(Factory Method Pattern):定义一个用于创建对象的接口,让子类决定实例化哪一个类,工厂方法使一个类的实例化延时到其子类.

prototype_pattern.py
原型模式(Prototype Pattern):用原型实例指定创建对象的种类,并且通过拷贝这些原型创建新的对象

template_method_pattern.py
模板方法模式(Template Method Pattern):定义一个操作中的算法骨架，将一些步骤延迟至子类中.模板方法使得子类可以不改变一个算法的结构即可重定义该算法的某些特定步骤

facade_pattern.py
外观模式(Facade Pattern):为子系统中的一组接口提供一个一致界面,此模式定义一个高层接口,使得子系统更加容易是用

builder_pattern.py
建造者模式(Builder Pattern):将一个复杂对象的构建与它的表示分离,使得同样的构建过程可以常见不同的表示

publish_subscribe_pattern.py
观察者模式(发布-订阅模式 Publish Subscribe Pattern):定义了一种一对多的关系，让多个观察对象同时监听一个主题对象，当主题对象状态发生变化时会通知所有观察者,是它们能够自动更新自己

abstract_factory_pattern.py
抽象工厂模式(Abstract Factory Pattern):提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们的类

state_pattern.py
状态模式(State Pattern):当一个对象的内在状态改变时允许改变其行为，这个对象看起来像是改变了其类

adapter_pattern.py
适配器模式(Adapter Pattern):将一个类的接口转换成为客户希望的另外一个接口.

memento_pattern.py
备忘录模式(Memento Pattern):不破坏封装性的前提下捕获一个对象的内部状态，并在该对象之外保存这个状态,这样已经后就可将该对象恢复到原先保存的状态

composite_pattern.py
组合模式(Composite Pattern):将对象组合成成树形结构以表示“部分-整体”的层次结构,组合模式使得用户对单个对象和组合对象的使用具有一致性.

iterator_pattern.py
迭代器模式(Iterator Pattern):提供方法顺序访问一个聚合对象中各元素，而又不暴露该对象的内部表示.

singleton_pattern.py
单例模式(Singleton Pattern):保证类仅有一个实例，并提供一个访问它的全局访问点.

bridge_pattern.py
桥接模式(Bridge Pattern):将抽象部分与它的实现部分分离，使它们都可以独立地变化.

command_pattern.py
命令模式(Command Pattern):将请求封装成对象，从而使可用不同的请求对客户进行参数化；对请求排队或记录请求日志，以及支持可撤消的操作.

chain_of_responsibility.py
职责链模式(Chain Of Responsibility):使多个对象都有机会处理请求，从而避免发送者和接收者的耦合关系。将对象连成链并沿着这条链传递请求直到被处理

mediator_pattern.py
中介者模式(Mediator Pattern):用一个对象来封装一系列的对象交互，中介者使各对象不需要显示地相互引用，从而使耦合松散，而且可以独立地改变它们之间的交互.

flyweight_pattern.py
享元模式(Flyweight Pattern):运用共享技术有效地支持大量细粒度的对象.

interpreter_pattern.py
解释器模式(Interpreter Pattern):给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子.
