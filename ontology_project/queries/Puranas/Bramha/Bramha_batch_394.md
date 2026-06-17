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

### Verse 1 (Bramha 0.7861)
- **Original**: आश्रम बतलाते हैं, उसके स्वरूपका वर्णन सुनो। सल्ध्या हो गयी, वहीं डेरा डाल देते हैं, ऐसे
- **Translation**: 

---

### Verse 2 (Bramha 0.7862)
- **Original**: भिश्षुको चाहिये कि पुत्र, धन, स्त्रीके प्रति स्नेहका लोगोंका सहारा और आधार गृहस्थ ही हैं।। त्याग करे और ईर्ष्यरहित होकर चतुर्थ आश्रममें पूर्वोक्त द्विज जब घरपर पधारें तो मधुर बाणीसे
- **Translation**: 

---

### Verse 3 (Bramha 0.7863)
- **Original**: जाय। उसीको संन्यास-आश्रम भी कहते हैं। * अतिथिर्षस्ष धग्माशों गृहात्‌ प्रतिनिवर्तते।स दत्वा दुष्कृतं तस्मे पुण्यमादाय गच्छति
- **Translation**: 

---

### Verse 4 (Bramha 0.7864)
- **Original**: (222। 36)
- **Translation**: 

---

### Verse 5 (Bramha 0.7865)
- **Original**: *उच्य वर्णकी अधोगति और नीच बर्णकी ऊर्ष्वगतिका कारण * 377 संन्यासीको समस्त जैवर्णिक कमाँके आरम्भका
- **Translation**: 

---

### Verse 6 (Bramha 0.7866)
- **Original**: घृणाकी दृष्टिसे देखे, क्योंकि अधिक आदर-सत्कार त्याग करना चाहिये। वह मित्र और शत्रुमें समान
- **Translation**: 

---

### Verse 7 (Bramha 0.7867)
- **Original**: मिलनेपर संन्यासी अन्य बन्धनोंसे मुक्त होनेपर भी भाव रखे। सब प्राणियोंका मित्र बना रहे। जरायुज
- **Translation**: 

---

### Verse 8 (Bramha 0.7868)
- **Original**: बँध जाता है। काम, क्रोध, दर्प, लोभ और मोह और अण्डज आदि किसी भी प्राणीके साथ मन,
- **Translation**: 

---

### Verse 9 (Bramha 0.7869)
- **Original**: आदि जितने दोष हैं, उन सबका त्याग करके वाणी और क्रियाद्वारा कभी द्रोह न करे। बह सब
- **Translation**: 

---

### Verse 10 (Bramha 0.7870)
- **Original**: संन्‍्यासी ममतारहित हो सर्वत्र बिचरता रहे।* प्रकारकी आसक्तियोंको त्याग दे। गाँवोमें एक गत
- **Translation**: 

---

### Verse 11 (Bramha 0.7871)
- **Original**: सम्पूर्ण प्राणियोंको अभय-दान देकर पृथ्वीपर विचरता और नगरमें पाँच रातसे अधिक न रहे। पशु, पक्षी
- **Translation**: 

---

### Verse 12 (Bramha 0.7872)
- **Original**: रहता है, उस देहाभिमानसे मुक्त यतिको कहीं भय आदिके प्रति न तो उसका राग हो और न द्वेष ही
- **Translation**: 

---

### Verse 13 (Bramha 0.7873)
- **Original**: नहीं होता। जो ब्राह्मण अस्निहोत्रको भावनाद्वारा रहे। जीवन-निर्वाहके लिये बह उच्च वर्णवाले
- **Translation**: 

---

### Verse 14 (Bramha 0.7874)
- **Original**: शरीरमें स्थापित करके अपने मुखमें भिक्षाप्रासत मनुष्योंके घरपर भिक्षाके लिये जाय--वह भी ऐसे
- **Translation**: 

---

### Verse 15 (Bramha 0.7875)
- **Original**: अन्नरूपी हविष्य डालकर उस शरीरस्थ अग्निको समयमें जब कि ससोईकी आग बुझ गयी हो और
- **Translation**: 

---

### Verse 16 (Bramha 0.7876)
- **Original**: आहुति देता है, वह उस संचित अग्रिके द्वारा उत्तम घरके सब लोग खा-पी चुके हों। भिक्षा न मिलनेपर
- **Translation**: 

---

### Verse 17 (Bramha 0.7877)
- **Original**: लोकोंमें जाता है। जो द्विज पवित्र एवं संयत बुद्धिसे खेद और मिलनेपर हर्ष न माने। भिक्षा उतनी ही
- **Translation**: 

---

### Verse 18 (Bramha 0.7878)
- **Original**: युक्त हो शास्त्रोक्त विधिसे मोक्ष-आश्रमका पालन ले, जिससे प्राणयात्रा होती रहे। विषयासक्तिसे बह
- **Translation**: 

---

### Verse 19 (Bramha 0.7879)
- **Original**: करता है, वह बिना ईंधनकी प्रज्यलित अग्निके नितान्त दूर रहे। अधिक आदर-सत्कारकी प्राप्तिको
- **Translation**: 

---

### Verse 20 (Bramha 0.7880)
- **Original**: सदृश शान्त तेजोमय त्रह्मलोकमें जाता है। # 306 डेटी 28 कम उच्च वर्णकी अधोगति और नीच वर्णकी ऊर्ध्वगतिका कारण घुनियोने पूछा--महाभाग! आप सर्वज्ञ हैं,
- **Translation**: 

---

