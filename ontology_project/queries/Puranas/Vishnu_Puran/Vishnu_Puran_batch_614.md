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

### Verse 1 (Vishnu Puran 0.12261)
- **Original**: तब विद्युत्से युक्त भयद्भूर गर्जना करनेवाले गजसमूहके समान बृहृदाकार संवर्तक नामक घोर मेघ आकाश्ममें उठते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.12262)
- **Original**: उनमेंसे कोई मेथ नील कमलके समान श्यामवर्ण, कोई कुमुद-कुसुमके समान श्वेत, कोई धूघ्रवर्ण और कोई पीतवर्ण होते हैं
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.12263)
- **Original**: कोई गधेके-से नर्णबाले, कोई लाखके-से रज्जबाले, कोई बैडूर्य-मणिके समान और कोई इन्द्रनीऊ- मणिके समान होते हैं
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.12264)
- **Original**: कोई शक्ब और कुन्दके समान थ्ैत-वर्ण, कोई जाती (चमेली) के समान उज्ज्वल और कोई कज्जलके समान इयामवर्ण, कोई इन्द्रगोपके समान रक्तवर्ण और कोई मयूरके समान विचित्र वर्णवाले होते हैं
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.12265)
- **Original**: क्येई गेरूके समान, कोई हरितालके समान और कोई महामेघ, नील-कण्टके पद्लके समान स्कवाले होते हैं
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.12266)
- **Original**: कोई नगरके समान, क्पेई पर्वतके समान और कोई कूटागार (गृहबिशेष) के समान बुहदाकार होते हैं तथा कोई पृथिवीतलके समान विस्तृत होते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.12267)
- **Original**: जे घनघोर शब्द करनेवाले महाकाय मेघगण आकाशको आच्छादित कर छेते हैं और मूसल्गधार जल बरसाकर त्रिल्लेकव्यापी भयद्भूर अग्निको जान्त कर देते हैं
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.12268)
- **Original**: हे मुनिश्रेष्ठ
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.12269)
- **Original**: ! अग्रिके नष्ट हो जानेपर भी अहर्निदा निरत्तर बरसते हुए वे मेघ सम्पूर्ण
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.12270)
- **Original**: आध्ड] घष्ठ अंझ ड33 धाराभिरतिमात्राभि: प्लावयित्वाखिलं भुवम्‌।
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.12271)
- **Original**: जगत्को जलमें डुबो देते हैं
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.12272)
- **Original**: हे ट्विज ! अपनी अति भुवलोंक॑ तथैबोध्ध्व॑ प्लावयन्ति हि ते द्विज
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.12273)
- **Original**: स्थ॒रू धाराओँसे भूलेकको जलगें डुबोकर वे भुवर्लेक तथा अन्धकारीकृते लोके नष्टे स्थावरजड्मे उसके भी ऊपरके छोकोंको भी जलमग्न कर देते हैं
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.12274)
- **Original**: इस प्रकार सम्पूर्ण संसारके अन्थक्रारमय हो जानेपर तथा वर्षन्ति ते महामेघा वर्षाणामधिक॑ शतम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.12275)
- **Original**: 40 समर स्थावर-जज्ञम जीवॉकि नष्ट हो जानेपर भी वे महामेघ एवं भवति कल्पान्ते समस्त मुनिसत्तम । वर्षसे अधिक कालतक बरसते रहते हैं
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.12276)
- **Original**: हे मुनिश्रे्‌ ः सनातन परमात्मा माहात्ययसे बासुदेवस्थ माहात्म्याश्नित्यस्थ परमात्मन:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.12277)
- **Original**: कल्पान्तमें इसी प्रकार यह समस्त विप्नत्र होता है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.12278)
- **Original**: चाचा हक उवणण-+-+> इति श्रीविष्णुपुराणे पष्टेंडशे तृतीयोउथ्याय:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.12279)
- **Original**: बजाज औ प--+5 चोथा अध्याय ब्राकृत प्रक्यका वर्णन अ्रीपराशर उवात्त श्रीपरादारजी खोल्ले--हे महामुने! जब जल सप्तर्षिस्थानमाक़म्य स्थितेउम्मसि महामुने । सप्तर्षियोंके स्थानको भी पार कर जाता है तो यह सम्पूर्ण एकार्णवं॑ भवत्येतत्लनैलोक्यमखिलं; ततः
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.12280)
- **Original**: 19 मुखनिः:श्वासजो विष्णोर्वायुस्ताज्ञलदांस्तत: । नाशयन्वाति मैत्रेय वर्षाणामपरं शतम्‌
- **Translation**: 

---

