# Manual Entity Extraction Prompt

Please extract entities (Deities, Concepts, Characters, Locations, Events) and their relationships from the following verses.
Return the output in strict JSON format.

## Valid Schema
- **Entity Types**: Deity, Concept, Character, Place, Event, Text
- **Relationship Types**: MENTIONS, IS_AVATAR_OF, RELATED_TO, LOCATED_AT, PARTICIPATED_IN

## JSON Format
```json
{
  "entities": [
    {"name": "EntityName", "type": "Type", "attributes": {"description": "..."}}
  ],
  "relationships": [
    {"from": "Entity1", "to": "Entity2", "type": "RELATION", "attributes": {"context": "..."}}
  ]
}
```

## Verses to Analyze

### Verse 1 (Vaivtpuran 16.3394)
- **Original**: शोक करनेकी क्या आवश्यकता है? कान्ते! तुम
- **Translation**: 

---

### Verse 2 (Vaivtpuran 16.3395)
- **Original**: श्षढड + संक्षि्त बहावैद्वर्तपुराण ] #%%$$%%$%$%%#% # %$ #%# # ##%%#$%%#%#% # %$#$%% %#$%%%#$# %ऋ %%ऋ$%%%ऊ#%%%%ऋ$% % %#$%% ##$% %%$%% %#%# %%# # % %$ # $ % %;# ऋ क भी अब शीघ्र ही इस शरीरका परित्याग करके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 16.3396)
- **Original**: था। परम सुन्दरी स्त्रियोंमें रत्न तुलसी सेवामें दिव्य रूप धारणकर श्रीहरिको पतिरूपसे प्राप्त उपस्थित थी। ज्ञानी शद्धुचूड़ने पुनः तुलसीकों कर लोगी। अतः तनिक भी घबरानेकी आवश्यकता
- **Translation**: 

---

### Verse 4 (Vaivtpuran 16.3397)
- **Original**: दिव्य ज्ञान प्रदर्शित करते हुए समझाया। साथ ही नहीं है। शह्डचूड़ने तुलसीको सम्पूर्ण शोकोंको दूर करनेवाले इस प्रकार शह्बुचूड़ तुलसीके साथ सुन्दर
- **Translation**: 

---

### Verse 5 (Vaivtpuran 16.3398)
- **Original**: उस उत्तम ज्ञानको बतलाया जो दिव्य भाण्डीरवनमें बातचीत कर रहा था, इतनेमें सायंकालका समय
- **Translation**: 

---

### Verse 6 (Vaivtpuran 16.3399)
- **Original**: भगवान्‌ श्रीकृष्णकी कृपासे उसे प्राप्त हुआ था। हो गया। रज्ञमय भवनमें पुष्प और चन्दनसे चर्चित
- **Translation**: 

---

### Verse 7 (Vaivtpuran 16.3400)
- **Original**: ऐसे श्रेष्ठ ज्ञाको पाकर उस देवीका मुख श्रेष्ठ शय्या बिछी थी। वह उसपर सो गया और
- **Translation**: 

---

### Verse 8 (Vaivtpuran 16.3401)
- **Original**: प्रसन्नतासे भर गया। समस्त जगत्‌ नश्वर है--यह भाति-भाँतिके बैभवोंकी बात उसके मनमें स्फुरित
- **Translation**: 

---

### Verse 9 (Vaivtpuran 16.3402)
- **Original**: मानकर वह हर्षपूर्वक हास-विलास करने लगी। होने लगी। उसके भवनमें रत्॒का दीपक जल रहा
- **Translation**: 

---

### Verse 10 (Vaivtpuran 16.3403)
- **Original**: फिर दोनों सुखपूर्वक सो गये। (अध्याय 17) #+“> >> >#ल्यआ 4200 00000 शद्डुचूड़का पुष्पभद्रा नदीके तटपर जाना, वहाँ भगवान्‌ शंकरके दर्शन तथा उनसे विशद बार्तालाप भगवान्‌ नारायण कहते हैं--नारद! राजा
- **Translation**: 

---

### Verse 11 (Vaivtpuran 16.3404)
- **Original**: सम्पत्ति, प्रजा एवं सेवकवर्ग, कोष तथा हाथी- शब्गुचूड़ श्रीकृष्फा भक्त था। वह ममनमें
- **Translation**: 

---

### Verse 12 (Vaivtpuran 16.3405)
- **Original**: घोड़े आदि वाहन सौंप दिये। उसने स्वयं कवच भगवान्‌ श्रीकृष्णका ध्यान करके ब्राह्ममुहूर्तमें ही
- **Translation**: 

---

### Verse 13 (Vaivtpuran 16.3406)
- **Original**: पहन लिया। हाथमें धनुष और बाण ले लिये। अपनी पुष्पमयी शय्यासे उठ गया। उसने स्वच्छ
- **Translation**: 

---

### Verse 14 (Vaivtpuran 16.3407)
- **Original**: सब सैनिकोंकों एकत्र किया। तीन लाख घोड़े जलसे स्त्रान करके रातके वस्त्र त्याग दिये। और पाँच लाख उत्तम श्रेणीके हाथी उपस्थित धुले हुए दो वस्त्रोंकोी पहनकर उज्ज्वल तिलक
- **Translation**: 

---

### Verse 15 (Vaivtpuran 16.3408)
- **Original**: हुए। दस हजार रथ तथा तीन-तीन करोड़ कर लिया; फिर इष्ट देवताके बन्दन आदि
- **Translation**: 

---

### Verse 16 (Vaivtpuran 16.3409)
- **Original**: धनुर्धारी, ढाल-तलवारधारी और त्रिशूलधारी प्रतिदिकके आवश्यक कर्त॑व्योंको पूरा किया।
- **Translation**: 

---

### Verse 17 (Vaivtpuran 16.3410)
- **Original**: वौर उसकी सेनाके अक्ल बने। दही, घृत, मधु और लाजा आदि माड्लिक
- **Translation**: 

---

### Verse 18 (Vaivtpuran 16.3411)
- **Original**: नारद! इस प्रकार दानवेश्वर शह्भचूड़ने वस्तुएँ देखीं। नारद! प्रतिदिनकी भाँति उसने अपरिमित सेना सजा ली। युद्धशास्त्रके पारगामी भक्तिपूर्वक ब्राह्मणोंकों उत्तम रत्न, मणि, स्वर्ण
- **Translation**: 

---

### Verse 19 (Vaivtpuran 16.3412)
- **Original**: एक महारथी वीरकों सेनापतिके पदपर नियुक्त और वस्त्र दान किये। यात्रा मड्गलमयों होनेके
- **Translation**: 

---

### Verse 20 (Vaivtpuran 16.3413)
- **Original**: किया। महारथी उसे समझना चाहिये जो लिये उसने अमूल्य रत्र तथा कुछ मोती, मणि
- **Translation**: 

---

