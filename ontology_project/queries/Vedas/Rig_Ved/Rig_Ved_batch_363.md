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

### Verse 1 (Rig Ved 0.7241)
- **Original**: जो याजक अभ्निदेव को हवि प्रदान करते हुए उनकी सेवा करते हैं, वे समस्त ऐश्वर्यों से सम्पन्न होकर प्रसिद्ध प्राप्त करते हैं। ऐसे याजक शक्तिशाली पुत्रों आदि से भी साम्पन्न होते हैं
- **Translation**: 

---

### Verse 2 (Rig Ved 0.7242)
- **Original**: 3167. अस्मे रायो दिवेदिये सं चरन्तु पुरुस्पृह:। अस्मे बाजास ईरताम्‌
- **Translation**: 

---

### Verse 3 (Rig Ved 0.7243)
- **Original**: अनेकों द्वारा स्पृहणीय ऐश्वर्य नित्य हमारे समीप आए । वे अग्निदेव हमारे यज्ञों में विविध प्रकार से धन- धान्य प्रदान करें
- **Translation**: 

---

### Verse 4 (Rig Ved 0.7244)
- **Original**: 3168. स विप्रश्नर्षणीनां शवसा मानुषाणाम्‌
- **Translation**: 

---

### Verse 5 (Rig Ved 0.7245)
- **Original**: अति क्षिप्रेव विध्यति
- **Translation**: 

---

### Verse 6 (Rig Ved 0.7246)
- **Original**: वे मेधावी अग्निदेव अपनी सामर्थ्य द्वारा मानवों के कष्टों को द्रुतगामी बाणों के सदृश तीक्ष्ण प्रहार करके पूर्णरूपेण नष्ट कर देते हैं
- **Translation**: 

---

### Verse 7 (Rig Ved 0.7247)
- **Original**: मे0 4 सुक्त 10 19 [सूक्त - 9 ] [ऋषि - वामदेव गौतम । देवता - अग्नि । छन्द - गायत्री
- **Translation**: 

---

### Verse 8 (Rig Ved 0.7248)
- **Original**: 3169. अग्ने पृछ महाँ असि य ईमा देवयुं जनम्‌
- **Translation**: 

---

### Verse 9 (Rig Ved 0.7249)
- **Original**: इयेथ बर्हिरासदम्‌
- **Translation**: 

---

### Verse 10 (Rig Ved 0.7250)
- **Original**: है अग्निदेव ! आप उपासकों को समृद्ध और सुखो बनाएँ, क्योंकि आप सामर्थ्यवान्‌ हैं- महान्‌ हैं । उपासक यजमपानों के समीप पवित्र कुश- आसन पर बैठने के लिये आप पधारें
- **Translation**: 

---

### Verse 11 (Rig Ved 0.7251)
- **Original**: 3170. स मानुषीषु दूलूभो विश्षु प्रावीरमर्त्य: । दूतो विश्वेषां भुवत्‌
- **Translation**: 

---

### Verse 12 (Rig Ved 0.7252)
- **Original**: असुरों द्वारा किये गये प्रहार जिनको नष्ट नहीं कर सकते, मनुष्यलोक में स्वतत्र रूप से बिचरने वाले वे अनश्चर अग्निदेव सम्पूर्ण देवताओं के दूत हैं
- **Translation**: 

---

### Verse 13 (Rig Ved 0.7253)
- **Original**: 3171, स सश परि णीयते होता मन्द्रो दिविष्टिषु । उत पोता नि घीदति
- **Translation**: 

---

### Verse 14 (Rig Ved 0.7254)
- **Original**: वे अग्निदेव यज्ञ मण्डप के चारों तरफ ले जाये जाते हैं । सोप्रयज्ञों में प्रार्थनीय वे अग्निदेव यज्ञ सम्पादक, होता तथा परिशोधक के रूप में विराजते हैं
- **Translation**: 

---

### Verse 15 (Rig Ved 0.7255)
- **Original**: 3172. उत ग्ना अग्निरध्वर उतो गृहपतिर्दमे
- **Translation**: 

---

### Verse 16 (Rig Ved 0.7256)
- **Original**: उत ब्रह्मा नि घीदति
- **Translation**: 

---

### Verse 17 (Rig Ved 0.7257)
- **Original**: वे अम्निदेव प्रार्थनीय एवं यज्ञादि कर्म सम्पन्न करने वाले होतारूप हैं । वे यज्ञ-मण्डप में गृहस्वामी तथा ब्रह्मा रूप में विद्यमान रहते हैं
- **Translation**: 

---

### Verse 18 (Rig Ved 0.7258)
- **Original**: 3173. वेषि ह्ाध्वरीयतामुपवक्ता जनानाम्‌
- **Translation**: 

---

### Verse 19 (Rig Ved 0.7259)
- **Original**: हव्या च मानुषाणाम्‌
- **Translation**: 

---

### Verse 20 (Rig Ved 0.7260)
- **Original**: है अग्निदेव ! आप यज्ञों में याजकों द्वारा प्रदत्त आहुतियों की अभिलाषा करते हैं । (यज्ञ में विद्यमान मनुष्यों को) श्रेष्ठ प्रेरणाएँ प्रदान करते हैं
- **Translation**: 

---

