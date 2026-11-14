/* Sedmica icons — Tabler Icons (MIT), mapped by semantic name */
import {
  IconFlame, IconCooker, IconMicrowave, IconSteam, IconPropeller, IconBlender, IconGrill,
  IconAcorn, IconBrandPeanut, IconMilk, IconEgg, IconWheat, IconFish, IconFishBone, IconSeeding,
  IconBowlSpoon, IconStack2, IconEggFried, IconBread, IconMilkshake, IconCake, IconSoup,
  IconToolsKitchen2, IconBowlChopsticks, IconMeat, IconBowl, IconSalad, IconBaguette, IconBurger,
  IconSun, IconMoon, IconSunrise, IconSunHigh, IconClock, IconUsers, IconRefresh, IconCheck,
  IconBasket, IconCarrot, IconCheese, IconGrain, IconSalt, IconChevronRight, IconChevronLeft,
  IconShare2, IconX, IconPlus, IconMinus, IconFlame as IconFire,
} from "@tabler/icons-react";

const MAP = {
  /* equipment */
  stove: IconFlame, oven: IconCooker, micro: IconMicrowave, multi: IconSteam,
  airfryer: IconPropeller, blender: IconBlender, grillpan: IconGrill,
  /* allergens */
  nuts: IconAcorn, peanut: IconBrandPeanut, milk: IconMilk, eggs: IconEgg,
  gluten: IconWheat, fish: IconFish, seafood: IconFishBone, soy: IconSeeding,
  /* food (recipe icons) */
  porridge: IconBowlSpoon, pancakes: IconStack2, egg: IconEggFried, sandwich: IconBread,
  cup: IconMilkshake, pie: IconCake, soup: IconSoup, stew: IconToolsKitchen2,
  pasta: IconBowlChopsticks, chicken: IconMeat, rice: IconBowl, salad: IconSalad,
  wrap: IconBaguette, patty: IconBurger, casserole: IconCake,
  /* shopping categories */
  "cat-meat": IconMeat, "cat-dairy": IconCheese, "cat-veg": IconCarrot,
  "cat-grocery": IconGrain, "cat-other": IconSalt,
  /* UI */
  sun: IconSun, moon: IconMoon, sunrise: IconSunrise, sunhigh: IconSunHigh,
  clock: IconClock, people: IconUsers, swap: IconRefresh, check: IconCheck,
  basket: IconBasket, right: IconChevronRight, left: IconChevronLeft,
  share: IconShare2, x: IconX, plus: IconPlus, minus: IconMinus, fire: IconFire,
};

export default function Icon({ name, size = 24, stroke = 1.7, className, style }) {
  const C = MAP[name] ?? IconToolsKitchen2;
  return <C size={size} stroke={stroke} className={className} style={style} aria-hidden="true" />;
}
