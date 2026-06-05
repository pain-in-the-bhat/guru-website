const controls = [
  {
    id: "price",
    label: "Sticker price",
    min: 22,
    max: 58,
    step: 1,
    unit: "$",
    lesson: "Lower it for dopamine. Raise it so the business can stay conscious."
  },
  {
    id: "growthSpend",
    label: "Bribes + ads",
    min: 0,
    max: 22,
    step: 0.5,
    unit: "$",
    lesson: "Useful for opening the door. Suspicious if it has to carry the furniture."
  },
  {
    id: "ops",
    label: "Boxes + border",
    min: 4,
    max: 24,
    step: 0.5,
    unit: "$",
    lesson: "The part of the internet that still involves rent, customs, and trucks."
  },
  {
    id: "factory",
    label: "Factory floor",
    min: 8,
    max: 34,
    step: 1,
    unit: "$",
    lesson: "The boring knob. Naturally, the important one."
  }
];

const presets = {
  growth: {
    note: "The app is cheap, the ads are loud, and the spreadsheet is asking for a cigarette.",
    price: 32,
    growthSpend: 13,
    ops: 10,
    factory: 16
  },
  balanced: {
    note: "The CFO has taken the marker away from growth. Fewer fireworks, fewer mysterious losses.",
    price: 39,
    growthSpend: 6,
    ops: 8,
    factory: 17
  },
  tariff: {
    note: "Customs looked up from lunch and noticed the business model. The border is now a character.",
    price: 41,
    growthSpend: 7,
    ops: 17,
    factory: 18
  },
  local: {
    note: "Delivery gets faster. The model also develops warehouse opinions and working-capital needs.",
    price: 44,
    growthSpend: 5,
    ops: 15,
    factory: 19
  }
};

const state = { ...presets.growth };
const sliderRoot = document.querySelector("#sliders");

function money(value) {
  const sign = value < 0 ? "-" : "";
  return `${sign}$${Math.abs(value).toFixed(value % 1 ? 1 : 0)}`;
}

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function compute() {
  const platformTake = state.price * 0.2;
  const contribution = platformTake - state.growthSpend - state.ops;
  const normalRetail = state.factory * 2.75 + 8.5;
  const priceGap = clamp((normalRetail - state.price) / normalRetail * 100, -30, 70);
  const pain = clamp(-contribution / 24 * 100, 0, 100);
  const score = clamp(priceGap * 1.25 + contribution * 3 + (state.factory <= 18 ? 12 : 0), 0, 100);

  return {
    contribution,
    normalRetail,
    priceGap,
    pain,
    score
  };
}

function grade(score) {
  if (score >= 82) return "A";
  if (score >= 66) return "B";
  if (score >= 48) return "C";
  if (score >= 30) return "D";
  return "F";
}

function buildControls() {
  sliderRoot.innerHTML = controls.map((control) => `
    <div class="lever">
      <div class="lever-top">
        <label for="${control.id}">${control.label}</label>
        <span class="lever-value" id="${control.id}Value">${money(state[control.id])}</span>
      </div>
      <input
        type="range"
        id="${control.id}"
        min="${control.min}"
        max="${control.max}"
        step="${control.step}"
        value="${state[control.id]}"
      >
      <p>${control.lesson}</p>
    </div>
  `).join("");

  controls.forEach((control) => {
    document.querySelector(`#${control.id}`).addEventListener("input", (event) => {
      state[control.id] = Number(event.target.value);
      document.querySelector(`#${control.id}Value`).textContent = money(state[control.id]);
      document.querySelectorAll("[data-preset]").forEach((button) => button.classList.remove("active"));
      document.querySelector("#presetNote").textContent = "Custom timeline. One meter will flatter you. The other will tell the truth.";
      render();
    });
  });
}

function setWidth(id, value) {
  document.querySelector(id).style.width = `${clamp(value, 2, 100)}%`;
}

function renderText(model) {
  const verdict = document.querySelector("#verdict");
  const read = document.querySelector("#modelRead");

  if (model.priceGap >= 30 && model.contribution < -8) {
    verdict.textContent = "Coupon Theater";
    read.textContent = "The customer is delighted. Finance is making direct eye contact. You made the bargain sing, but it is being autotuned by subsidy and ads.";
  } else if (model.priceGap >= 22 && model.contribution >= -4) {
    verdict.textContent = "Suspiciously Viable";
    read.textContent = "This is the zone everyone claims they are in: cheap enough to feel weird, disciplined enough to maybe be real.";
  } else if (state.ops >= 16) {
    verdict.textContent = "Customs Killed The Vibe";
    read.textContent = "The border found the invoice and brought friends. Tariffs, compliance, and warehouses are where cute cross-border stories learn paperwork.";
  } else if (model.priceGap < 14) {
    verdict.textContent = "Normal Retail With Extra Steps";
    read.textContent = "You cleaned up the economics by sanding off the weirdness. Now you are competing on trust, delivery, selection, and fewer dopamine fireworks.";
  } else if (state.growthSpend >= 14) {
    verdict.textContent = "Rented Demand";
    read.textContent = "Ads and subsidy are doing jazz hands near a burn chart. If every order needs a bribe, the marketplace has not earned demand yet.";
  } else {
    verdict.textContent = "Annoyingly Plausible";
    read.textContent = "Not dead. Not genius. The real question is whether cheapness comes from system efficiency, or from hiding losses in better-looking pockets.";
  }
}

function render() {
  const model = compute();
  const score = Math.round(model.score);

  document.querySelector("#grade").textContent = grade(score);
  document.querySelector("#factoryValue").textContent = money(state.factory);
  document.querySelector("#priceValue").textContent = money(state.price);
  document.querySelector("#growthSpendValue").textContent = money(state.growthSpend);
  document.querySelector("#opsValue").textContent = money(state.ops);
  document.querySelector("#marginValue").textContent = money(model.contribution);
  document.querySelector("#priceGap").textContent = `${Math.round(model.priceGap)}%`;
  document.querySelector("#painScore").textContent = `${Math.round(model.pain)}%`;

  setWidth("#priceFill", model.priceGap * 1.45);
  setWidth("#painFill", model.pain);
  renderText(model);
}

document.querySelectorAll("[data-preset]").forEach((button) => {
  button.addEventListener("click", () => {
    const presetName = button.dataset.preset;
    Object.assign(state, presets[presetName]);
    document.querySelector("#presetNote").textContent = presets[presetName].note;
    document.querySelectorAll("[data-preset]").forEach((item) => item.classList.toggle("active", item === button));
    controls.forEach((control) => {
      const input = document.querySelector(`#${control.id}`);
      input.value = state[control.id];
      document.querySelector(`#${control.id}Value`).textContent = money(state[control.id]);
    });
    render();
  });
});

buildControls();
document.querySelector('[data-preset="growth"]').classList.add("active");
render();
