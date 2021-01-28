% Глобальная структура, содержащая индексы переменных в общем векторе состояния ракеты. Глобальные переменные доступны в функциях.
global u_range;
global state;
global log;

u_range = struct();
u_range.m = 1;      % Масса ракеты
u_range.r = 2:3;    % Вектор местоположения ракеты
u_range.v = 4:5;    % Вектор скорости ракеты
u_range.alpha = 6;  % Угол наклонения ракеты
u_range.omega = 7;  % Угловая скорость вращения ракеты
u_range.size = [7, 1];  % Размер вектора состяния

% Структура, хранящая фазы полёта и управляющие воздействия
state = struct();

% Таблицы для хранения зависимости параметров расчёта от времени. 
% В данных таблицах будут храниться значения, не входящие в вектор состояния ракеты u.
log.state = table();
log.phases = table();

u0 = zeros(u_range.size);   % Вектор начального состояния - столбец из нулей
u0(u_range.m) = 20e3;       % Задание стартовой массы ракеты с учётом топлива

% Установка начальных значений состояния ракеты
state.phase = 0;
state.phaseStart = 0;
state.subPhase = 0;
state.subPhaseStart = 0;
state.phaseStarted = false;

% Проверка управляющей функции без моделирования полёта
for t = 0:600
    % Вызов управляющей функции
    falcon_controlFcn(t, u0);
    
    % Сохранение состояния в таблицу
    log.state = [log.state; struct2table(state)];
end

% Отображение фрагментов таблиц
disp(log.phases(1:3,:));
disp(log.state);

% Извлечение полей структуры в отдельные переменные для автоматической проверки Grader
log_phases = log.phases;
log_state = log.state;

function falcon_controlFcn(t, u)

global state log;

switch state.phase
case 0
state.massFlow = -20;
state.beta = 0;
if ~state.phaseStarted
state.phaseStart = t;
state.subPhaseStart = t;
state.phaseStarted = true;
row = struct();
row.phase = state.phase;
row.subPhase = state.subPhase;
row.description = 'Вертикальный взлёт';
row.t = t;
log.phases = [log.phases; struct2table(row)];
end
if t - state.phaseStart >=80
state.phase = 1;
state.subPhase = 0;
state.phaseStarted = false;
end

case 1
state.massFlow = -20;
switch state.subPhase
case 0
state.beta = -0.0001;
if ~state.phaseStarted
startPhase(t, 'Создание момента для начала вращения', false);
end

if t-state.subPhaseStart >=40
switchPhase(1,1);
end

case 1
state.beta=0;
if ~state.phaseStarted
startPhase(t, 'Свободное вращение', false);
end

if t-state.subPhaseStart >=80
switchPhase(1,2);
end
case 2
state.beta = 0.00007;
if ~state.phaseStarted
startPhase(t, 'Создание момента для остановки вращения', false);
end
if t-state.subPhaseStart >=40
switchPhase(1,3);
end
case 3
state.beta = 0;
if ~state.phaseStarted
startPhase(t, 'Набор горизонтальной скорости', false);
end
if t>500
    switchPhase(2,0);
end
end

case 2
state.massFlow = 0;
state.beta = 0;
if ~state.phaseStarted
    startPhase(t, 'Свободный полёт', true);
end
end

end

function startPhase(t, description, phaseSwitched)

global state log;
if (phaseSwitched)
    state.phaseStart = t;
end

state.subPhaseStart = t;
state.phaseStarted = true;
row = struct();
row.phase = state.phase;
row.subPhase = state.subPhase;
row.description = cellstr(description);
row.t = t;
log.phases = [log.phases; struct2table(row)];

end

function switchPhase(phase, subPhase)

global state;
state.phase = phase;
state.subPhase = subPhase;
state.phaseStarted = false;
end