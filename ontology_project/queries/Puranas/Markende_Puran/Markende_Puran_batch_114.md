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

### Verse 1 (Markende Puran 0.2261)
- **Original**: सयनश्रितर्य जज्ञे तथा पावकतेजसा
- **Translation**: 

---

### Verse 2 (Markende Puran 0.2262)
- **Original**: श्रुया ज्ञ स॑ध्यवोस्तेज: श्रवणावनिलस्थ चञञ। 287 # 686 44 85447 #4777 78 क 7 हु अं 273: 5554 अन्येषां चैंब देबानां सम्भवस्तेजर्सा शिवा
- **Translation**: 

---

### Verse 3 (Markende Puran 0.2263)
- **Original**: इस प्रकार देकताओंके ज्चन सुनकर भगवान्‌ विष्णु और शिवने दैत्योंपर बड़ा क्रोध किया। उनकी भौंहें तन गयीं और मुँह टेड्डा हो गया
- **Translation**: 

---

### Verse 4 (Markende Puran 0.2264)
- **Original**: तब अत्यन्त कोपमें भरे हुए चक्रपाणि श्रीविष्णुके मुखसे एक महायू तेज प्रकट हुआ। इसी प्रकार ब्रह्मा, शंकर तथा इन्द्र आदि अन्याग्य देवताओके शरीरसे भी बड़ा भारी त्तेज तिकला। बह सब मिलकर एक हो गया
- **Translation**: 

---

### Verse 5 (Markende Puran 0.2265)
- **Original**: महान्‌ तेजका बह पुञ्ञ जाज्वत्यमार पर्वत सा जान पड़ा। देवताओं ने देखा, वहाँ उसकी ज्वालाएँ सम्पूर्ण दिशाओंमें व्याप्त हो रही थीं
- **Translation**: 

---

### Verse 6 (Markende Puran 0.2266)
- **Original**: सप्पूर्ण देवताओंके शरीरसे प्रकट हुए उस तेजको कहीं तुलना नहीं थी। एकत्रित होनेपर बह एक नारीके रूपमें परिणत हो गया और अपने ग्रकाशसे तीनों लोकोमें व्याप्त जान पड़ा
- **Translation**: 

---

### Verse 7 (Markende Puran 0.2267)
- **Original**: भगवान्‌ शंकरका जो त्तेज था, उससे उस देवीका मुख प्रकट हुआ। बमणजके तेजसे उसके सिरमें जाल दिकल आदे। श्रीविष्णुभगवान्‌के तेजसे ठसकी भुजाएँ उत्पन्न हुई
- **Translation**: 

---

### Verse 8 (Markende Puran 0.2268)
- **Original**: चन्द्रमाके 822
- **Translation**: 

---

### Verse 9 (Markende Puran 0.2269)
- **Original**: 188 * सैक्षिम मार्कणडयपुराण * 14456 6388 8 # 6557 # #+6:<::005+ 9 +
- **Translation**: 

---

### Verse 10 (Markende Puran 0.2270)
- **Original**: 5 4 & & #&£ 6755 # # #&+%+::6:07%%:+% &
- **Translation**: 

---

### Verse 11 (Markende Puran 0.2271)
- **Original**: 6& 4:42 77 0 % # #<&:#:2:#7-+ * % 6 & 66 2:07 # «+ 4 6... 3.26% तेजसे दोनों स्तनॉंका और इन्द्रके तेजते मध्यभाग! अददज्जलधिस्तस्थै पद्चुजं चातिशोभनप्‌। (कटिग्रदेश)-का प्रादुर्घाध हुआ। दरुणके तेजसे हिमसान्‌ वाहन सिंहँ रत्तानि खिसिधानि च
- **Translation**: 

---

### Verse 12 (Markende Puran 0.2272)
- **Original**: जड़ा और पिंडली तथा पृष्लोके तेजसे नितस्नभाग
- **Translation**: 

---

### Verse 13 (Markende Puran 0.2273)
- **Original**: दद्ावशून्य॑ सुरया पानपात्रं थनाथिप:। प्रकट हुआ
- **Translation**: 

---

### Verse 14 (Markende Puran 0.2274)
- **Original**: ब्रह्मके त्ेजसे दोनों बएण और
- **Translation**: 

---

### Verse 15 (Markende Puran 0.2275)
- **Original**: शेषश्ष सर्वनागेशो महाम्रणिविभूषितम्‌
- **Translation**: 

---

### Verse 16 (Markende Puran 0.2276)
- **Original**: । सूर्यके तेजस़ते उनको अँगुलियाँ हुई। वसुओके तेजसे नागहार॑ ददौ तस्थै धत्ते यः पृथ्चिवीमिमाम्‌। 8थोंकी अँगुलियाँ और कुबेरके तेजसे नासिका प्रकट
- **Translation**: 

---

### Verse 17 (Markende Puran 0.2277)
- **Original**: अन्यैरपि. सुरैदेंसी. भूषणरायुवैस्तथा
- **Translation**: 

---

### Verse 18 (Markende Puran 0.2278)
- **Original**: उस देवीके दाँत प्रजापतिके तेजसे और
- **Translation**: 

---

### Verse 19 (Markende Puran 0.2279)
- **Original**: स्रम्मानिता ननादोच्नै: साडूहास॑ मुहर्मृहः। त्ोनों नेत्र आनिके तेजसे प्रकट हुए थे
- **Translation**: 

---

### Verse 20 (Markende Puran 0.2280)
- **Original**: तस्मा चादेन घोरेण कृत्स्नमापूरिते नभः
- **Translation**: 

---

