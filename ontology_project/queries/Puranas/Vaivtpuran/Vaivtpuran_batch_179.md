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

### Verse 1 (Vaivtpuran 13.2949)
- **Original**: ही ब्रह्मारूपसे सदा संसारकी सृष्टि करता हूँ और था। राजा वृषध्वजकी भगवान्‌ नारायण, लक्ष्मी
- **Translation**: 

---

### Verse 2 (Vaivtpuran 13.2950)
- **Original**: शंकररूपसे संहार। मैं ही शिव हूँ। तुम भी मेरे और सरस्वती-इनमें किसीके प्रति श्रद्धा नहीं
- **Translation**: 

---

### Verse 3 (Vaivtpuran 13.2951)
- **Original**: ही रूप हो और ये शंकर भी मुझसे भिन्न नहीं थी। उसने सम्पूर्ण देवताओंका पूजन त्याग दिया
- **Translation**: 

---

### Verse 4 (Vaivtpuran 13.2952)
- **Original**: हैं। मैं ही नाना रूप धारण करके सृष्टि और था। अभिमानमें चूर होकर बह भाद्रमासमें
- **Translation**: 

---

### Verse 5 (Vaivtpuran 13.2953)
- **Original**: पालनकी व्यवस्था किया करता हूँ। देवताओं! महालक्ष्मीकी पूजामें विघ्न उपस्थित किया करता
- **Translation**: 

---

### Verse 6 (Vaivtpuran 13.2954)
- **Original**: तुम्हाश कल्याण हो; जाओ, अब तुम्हें भय नहीं था। माघकी शुक्ल पञ्ममीके दिन समस्त देवता
- **Translation**: 

---

### Verse 7 (Vaivtpuran 13.2955)
- **Original**: होगा। मैं वचन देता हूँ, आजसे शंकरका भय सरस्वतीकी विस्तृतरूपसे पूजा करते थे; परंतु
- **Translation**: 

---

### Verse 8 (Vaivtpuran 13.2956)
- **Original**: तुम्हारे पास नहीं आ सकेगा। वे सर्वेश भगवान्‌ + स्मरन्ति ये यत्र तत्र मां विपत्ौ भयान्विता: । तांस्तत्र गत्वा रक्षामि चक्रहस्तस्त्वरान्वित:
- **Translation**: 

---

### Verse 9 (Vaivtpuran 13.2957)
- **Original**: (प्रकृतिखण्ड 13। 20)
- **Translation**: 

---

### Verse 10 (Vaivtpuran 13.2958)
- **Original**: 138 + संक्षिप्त ब्रह्मबैवर्तपुराण * शंकर सत्पुरुषोंके स्वामी हैं। उन्हें भक्तात्मा और
- **Translation**: 

---

### Verse 11 (Vaivtpuran 13.2959)
- **Original**: स्वच्छ चँवर डुलाकर उनकी सेवा कर रहे थे। भक्तवत्सल कहा जाता है और बे सदा भक्तोंके
- **Translation**: 

---

### Verse 12 (Vaivtpuran 13.2960)
- **Original**: नारद! उनका सम्पूर्ण अड्भ दिव्य चन्दनोंसे अधोन रहते हैं। ब्रह्मन्‌ ! सुदर्शनचक्र और भगवान्‌
- **Translation**: 

---

### Verse 13 (Vaivtpuran 13.2961)
- **Original**: अनुलिप्त था। वे अनेक प्रकारके भूषण और शंकर-ये दोनों मुझे प्राणोंसे भी बढ़कर प्रिय
- **Translation**: 

---

### Verse 14 (Vaivtpuran 13.2962)
- **Original**: पीताम्बर धारण किये हुए थे। लक्ष्मीका दिया हैं। ब्रह्माण्डमें इनसे अधिक दूसरा कोई तेजस्वी
- **Translation**: 

---

### Verse 15 (Vaivtpuran 13.2963)
- **Original**: हुआ ताम्बूल उनके मुखमें शोभा पा रहा था। नहीं है। ये शंकर चाहें तो लीलापूर्वक करोड़ों
- **Translation**: 

---

### Verse 16 (Vaivtpuran 13.2964)
- **Original**: ऐसे प्रभुकों देखकर भगवान्‌ शंकरका मस्तक सूर्योकों प्रकट कर सकते हैं। करोड़ों ब्रह्माओंके
- **Translation**: 

---

### Verse 17 (Vaivtpuran 13.2965)
- **Original**: उनके चरणोंमें झुक गया। ब्रह्माने शंकरकों प्रणाम निर्माणकी भी इनमें पूर्ण सामर्थ्य है। इन
- **Translation**: 

---

### Verse 18 (Vaivtpuran 13.2966)
- **Original**: किया तथा अत्यन्त डरते हुए सूर्य भी शंकरको त्रिशूलधारी भगवान्‌ शंकरके लिये कोई भी कार्य
- **Translation**: 

---

### Verse 19 (Vaivtpuran 13.2967)
- **Original**: प्रणाम करने लगे। कश्यपने अतिशय भक्तिके असाध्य नहीं; तथापि कुछ भी बाहरी ज्ञान न
- **Translation**: 

---

### Verse 20 (Vaivtpuran 13.2968)
- **Original**: साथ स्तुति और प्रणाम किया। तदनन्तर भगवान्‌ रखकर ये दिन-रात मेरे ही ध्यानमें लगे रहते शिव सर्वेश्वर श्रीहरिकी स्तुति करके एक सुखमय हैं। अपने पाँच मुखोंसे मेरे मन्त्रोंका जप करना
- **Translation**: 

---

