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

### Verse 1 (Bhagwat_Geeta 13.1134)
- **Original**: 166 * श्रीमद्धगवद्रीता * देनेवाला है; तथा जो योगी निरन्तर संतुष्ट है, मन- इन्द्रियोंसहित शरीरको वशमें किये हुए है और मुझमें दृढ़ निश्चयवाला है--वह मुझमें अर्पण किये हुए मन- बुद्धिवाला मेरा भक्त मुझको प्रिय है
- **Translation**: 

---

### Verse 2 (Bhagwat_Geeta 13.1135)
- **Original**: यस्मान्नोद्विजते लोको लोकान्नोद्विजते च यः । हर्षामर्षभयोद्वेगैर्मुक्ती यः स च मे प्रिय:
- **Translation**: 

---

### Verse 3 (Bhagwat_Geeta 13.1136)
- **Original**: जिससे कोई भी जीव उद्देगको प्राप्त नहीं होता और जो स्वयं भी किसी जीवसे उद्देगको प्राप्त नहीं होता; तथा जो हर्ष, अमर्ष*, भय और उद्देगादिसे रहित है--वह भक्त मुझको प्रिय है
- **Translation**: 

---

### Verse 4 (Bhagwat_Geeta 13.1137)
- **Original**: अनपेक्ष: शुचिर्दक्ष उदासीनो गतव्यथः। सर्वारम्भपरित्यागी यो मद्धक्तः स मे प्रिय:
- **Translation**: 

---

### Verse 5 (Bhagwat_Geeta 13.1138)
- **Original**: जो पुरुष आकांक्षासे रहित, बाहर-भीतरसे शुद्ध* चतुर, पक्षपातसे रहित और दुःखोंसे छूटा हुआ है--वह सब आरमभ्भोंका त्यागी मेरा भक्त मुझको प्रिय है
- **Translation**: 

---

### Verse 6 (Bhagwat_Geeta 13.1139)
- **Original**: यो न हृष्यति न द्वेष्टि न शोचति न काड्श्षति। शुभाशुभपरित्यागी भक्तिमान्य: स मे प्रिय:
- **Translation**: 

---

### Verse 7 (Bhagwat_Geeta 13.1140)
- **Original**: जो न कभी हर्षित होता है, न द्वेष करता है, न 1. दूसरेकी उन्नतिको देखकर संताप होनेका नाम “अमर्ष' है। 2. गीता अध्याय 13 श्लोक 7 की टिप्पणीमें इसका विस्तार देखना चाहिये।
- **Translation**: 

---

### Verse 8 (Bhagwat_Geeta 13.1154)
- **Original**: * अध्याय 13* 1269 जानना है*, वह ज्ञान है--ऐसा मेरा मत है
- **Translation**: 

---

### Verse 9 (Bhagwat_Geeta 13.1155)
- **Original**: तत्क्षेत्र यच्च यादूक्‍च यद्विकारि यतश्च यत्‌ । सच यो यत्प्रभावश्च तत्समासेन मे श्रुणु
- **Translation**: 

---

### Verse 10 (Bhagwat_Geeta 13.1156)
- **Original**: वह क्षेत्र जो और जैसा है तथा जिन विकारोंवाला है, और जिस कारणसे जो हुआ है; तथा वह क्षेत्रज्ञ भी जो और जिस प्रभाववाला है--वह सब संक्षेपमें मुझसे सुन
- **Translation**: 

---

### Verse 11 (Bhagwat_Geeta 13.1157)
- **Original**: ऋषिभिर्बहुधा गीतं छन्दोभिविंविधे: पृथक्‌ । ब्रह्मसूत्रपदेश्चैव हेतुमद्धधिर्विनिश्चितैः
- **Translation**: 

---

### Verse 12 (Bhagwat_Geeta 13.1158)
- **Original**: यह क्षेत्र और क्षेत्रज्ञका तत्त्व ऋषियोंद्वारा बहुत प्रकारसे कहा गया है और विविध वेदमन्त्रोंद्रारा भी विभागपूर्वक कहा गया है तथा भलीभाँति निश्चय किये हुए युक्तियुक्त ब्रह्मसूत्रके पदोंद्वार भी कहा गया है
- **Translation**: 

---

### Verse 13 (Bhagwat_Geeta 13.1159)
- **Original**: महाभूतान्यहड्डारो बुद्धिरव्यक्तमेव च। इन्द्रियाणि दशैकं॑ च पञ्ञ चेन्द्रियगोचरा:
- **Translation**: 

---

### Verse 14 (Bhagwat_Geeta 13.1160)
- **Original**: पाँच महाभूत, अहंकार, बुद्धि और मूल प्रकृति भी तथा दस इन्द्रियाँ, एक मन और पाँच इन्द्रियोंक विषय अर्थात्‌ शब्द, स्पर्श, रूप, रस और गन्ध--
- **Translation**: 

---

### Verse 15 (Bhagwat_Geeta 13.1161)
- **Original**: इच्छा द्वेष: सुखं दुःखं सद्भगतश्चेतना धृति: । एतक्क्षेत्रं समासेन सविकारमुदाहतम्‌
- **Translation**: 

---

### Verse 16 (Bhagwat_Geeta 13.1162)
- **Original**: । +* गीता अध्याय 13 श्लोक 23 और उसकी टिप्पणी देखनी चाहिये।
- **Translation**: 

---

### Verse 17 (Bhagwat_Geeta 13.1168)
- **Original**: * अध्याय 13* 171 अभाव और अहंकारका भी अभाव, जन्म, मृत्यु, जरा और रोग आदियमें दुःख और दोषोंका बार-बार विचार करना
- **Translation**: 

---

### Verse 18 (Bhagwat_Geeta 13.1169)
- **Original**: असक्तिरनभिष्वड्ः पुत्रदारगृहादिषु। नित्यं च समचित्तत्वमिष्टानिष्टोपपत्तिषु
- **Translation**: 

---

### Verse 19 (Bhagwat_Geeta 13.1170)
- **Original**: पुत्र, स्‍त्री, घर और धन आदिमें आसक्तिका अभाव, ममताका न होना तथा प्रिय और अप्रियकी प्राप्तिमें सदा ही चित्तका सम रहना
- **Translation**: 

---

### Verse 20 (Bhagwat_Geeta 13.1171)
- **Original**: मयि चानन्ययोगेन भक्तिरव्यभिचारिणी। विविक्तदेशसेवित्वमरतिर्जनसंसदि
- **Translation**: 

---

