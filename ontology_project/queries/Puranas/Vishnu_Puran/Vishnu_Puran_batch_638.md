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

### Verse 1 (Vishnu Puran 0.12741)
- **Original**: हे द्विजोत्तम ! जब योगी सबाीज प्राणायामका अध्यास आरम्भ करता है तो उसका अलाबन भगवान्‌ अनचक्तका हिएण्यगर्भ आदि स्थूलरूप होता है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12742)
- **Original**: तदनत्तर वह प्रत्याहाएका अध्यास करते हुए दाब्दादि विषयोमें अनुरक्त हुई अपनी इन्द्रियोक्त् ग्रेककर अपने चित्तव्ती अनुगामिनी बनाता है
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12743)
- **Original**: ऐसा ऊरनेसे अत्यन्त चक्कल ईन्द्रियाँ उसके खशीभूत हो जाती हैं। इन्द्रियोंको बशमें किये बिना कोई योगी योग- साधन नहीं कर सकता
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12744)
- **Original**: इस प्रव्यर प्राणायामसे वायु और प्रत्याहारसे इद्धियोंक्ो कशीधूत करके चित्तको उसके शुभ आश्रयमें स्थित करे
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12745)
- **Original**: डछ0 स्काष्डिका उताच कथ्यतां मे महाभाग चेतसो यहशुभाश्रय: । यदाधारमशेर्ष तद्धन्ति दोषमस्त्रेद्धघम
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12746)
- **Original**: <8 केशिध्वज उनाच आश्रबश्चेतसो ब्रह्म द्विधा तश स्वभावत: । भूष मूर्त्तमपूर्त च॑ पर॑चापरमेत ता
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12747)
- **Original**: 47 त्रिविधा भावना भूष विश्वमेतत्रिबरोधताम्‌। ब्रह्माख्या कर्पसेज्ञा च तथा चैवो भयात्मिका
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12748)
- **Original**: 48 कर्मभावात्पिका ह्वोका ब्रह्मभावात्मिका परा । उभवात्पिका तप्रैवान्या ब्रिविधा भावभावना
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12749)
- **Original**: 49 सननन्‍्दनादयों ये तु ब्रह्ममावनया युता: । कर्मभावनया चान्ये देवाद्या: स्थावराश्षरा:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12750)
- **Original**: 50 हिरण्यगर्भादिषु च ब्रह्मकर्मात्पिका द्विधा । बोधाधिकारयुक्तेचु विद्यते भावभावना
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12751)
- **Original**: 51 अक्षीणेष॒ समस्तेषु॒विशेषज्ञानकर्मसु । विश्वमेतत्पर॑चान्यज्रेदभिन्नदृशशा नृणाम्‌
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12752)
- **Original**: 52 प्रत्यस्तमितभेद॑ _यत्सत्तामात्रमगोचरम्‌ । बचसामात्मसंलेध्ध तज्ज्ञान॑ ब्रह्मसंज्नितम
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12753)
- **Original**: 53 तच विष्णो: परं रूपभरूपाख्यमनुत्तमम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12754)
- **Original**: विश्वस्वरूपवैरूप्यलक्षणं... परपात्मन:
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12755)
- **Original**: पड न तद्योगयुजा शक्‍ये नृप चिन्तयितुं यतः । ततः स्थूल हरे रूप चिन्तयेद्विश्वगोच्चरम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12756)
- **Original**: 55 हिरण्यगर्भों भगवान्वासुदेव: प्रजापति: । मरुतो बसलो रुद्भा भास्करास्तारका ग्रहा:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12757)
- **Original**: 56 गन्धर्वयक्षदैत्याद्याससकला. देवयोनय: । मनुष्या: पशवइचझैल्लास्समुद्रास्सरितो ब्रुमा:
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12758)
- **Original**: 597 भूष भूतान्यशेषाणि भूतानां ये च हेतवः । प्रथानादिविशेषान्त चेतनाचेतनात्यकम्‌
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12759)
- **Original**: 58 एकपादं द्विपादं च बहुपादमपादकम । मूर्तपेतद्धे रूप. भावनात्रितयात्यकम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12760)
- **Original**: 59 एतत्सर्वपरिद॑ विश्व जगदेतश्चराचरम्‌ । परब्रह्मस्वरूपस्थ विष्णोइशक्तिसमन्वितम्‌
- **Translation**: 

---

