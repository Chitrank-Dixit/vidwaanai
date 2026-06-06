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

### Verse 1 (Vishnu Puran 0.9781)
- **Original**: ! श्रीपराश्रजी बोले--कृष्णचन्द्रके ऐसा कहनेपर देवराज इन्द्र उसका आलिफ्डन कर ऐरावत हाथीपर आरूढ हो ख्वर्गको चले गये
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.9782)
- **Original**: तदनत्तर कृष्णचद्र भी गोपियोंके दृष्टिपातसे पवित्र हुए मार्गद्गाश गोपकुमारों और गौओंके साथ त्रजको लौट आये
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.9783)
- **Original**: अशप्पममम है $ लय इति श्रोविष्णुपुराणे पञ्ममेंडशे द्वादशोऊध्याय:
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.9784)
- **Original**: ब्न--- और +---
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.9785)
- **Original**: आ* 13 । पश्चम अंश 343 तेरहवाँ अध्याय गोपोंद्वारा भगवानका प्रप्माबवर्णन तथा भगवान्‌का गोपियोंके साथ रासक्रीडा करना श्रीपराझर उवाच गते झक्रे तु गोपालाः कृष्णमक्तिकारिणम्‌ । ऊद्चुः प्रीत्या धृत दृष्ठा तेन गोवर्धनाचछप्‌
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.9786)
- **Original**: 1 बयमस्मात्महाभाग भगवन्पहतो भयात्‌। गावश्च भवता त्राता गिरिधारणकर्मणा
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.9787)
- **Original**: 2 बालक्रीडेयमतुला गोपालत्वं जुगुप्सितम्‌। दिव्यं च भवत: कर्म किमेतत्तात कथ्वताम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.9788)
- **Original**: 3 कालियो दमितस्तोये धेनुको ब्रिनिपातित: । घृतो गोवर्धनश्ार्य शद्धितानि मनांसि न:
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.9789)
- **Original**: 4 सत्य सत्यं हरेः पादो शपामोउमितविक्रम । यधावददीर्यमात्म्ेक्य न त्वां मन्‍्यामहे नरम
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.9790)
- **Original**: 57 प्रीति: सस्त्रीकुमारस्य ब्रजस्य त्वयि केशव । कर्म चेदमशक्यं यत्समस्तैख्िदवौरपि
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.9791)
- **Original**: & बालत्व चातिवीर्यत्व जन्म चास्पास्वशो भनम्‌ । चिन्त्यमानममेयात्मज्छड्डां कृष्ण प्रयच्छति
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.9792)
- **Original**: 7 देवो वा दानवो वा वे यक्षो गन्धर्व एवं वा । किमस्माकं विचारेण बान्धवोउसि नमोस्तु ते
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.9793)
- **Original**: «8 औपदजर उवाच क्षणं भूत्वा त्वसौ तृष्णी कि्लचित्रणयकोपवान्‌ । इत्येवमुक्तस्तैगोंपै: कृष्णो5ष्याह महामति:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.9794)
- **Original**: 9 अभगचानुकाच मत्सम्बन्धेन वो गोपा यदि छज्जा न जायते । हल्म्रध्यों वाहं तत: कि वो विचारेण प्रयोजनम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.9795)
- **Original**: 10 यदि वो5स्ति मयि प्रीति: शलाघ्यो है भवर्ता यदि । तदात्मबन्धुसदृशी बुद्धिर्व: क्रियतां मयि
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.9796)
- **Original**: 11 श्रीपराशरजी बखोले--इन्द्रक: चले जानेपर ल्ील्अणिहारी श्रीकृष्णच्तन्द्रको बिना प्रवास हो गोवर्धन- पर्वत धारण करते देख गोपगण उनसे. प्रीतिपूर्वक बोले--
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.9797)
- **Original**: हे भगवन्‌ ! हे महाभाग ! आपने गिरिराजकों धारण कर हमारी और गौऑकी इस महान्‌ भयसे रक्षा की है
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.9798)
- **Original**: है तात ! कहाँ आपकी यह अनुपम वाललीस्ग्, कहाँ निन्दित गोपजाति और कहाँ ये दिव्य कर्म ? यह सब क्या है, कृपया हमें बतल्वइये
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.9799)
- **Original**: आपने यमुनाजलमें काल्म्यिनागका दमन किया, घेनुकासुरको मारा और फिर यह गोवर्धनपर्वत धारण किया; आपके इन अद्भुत कर्मोंसे हमारे चित्तमें बड़ी झॉंका हो रही है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.9800)
- **Original**: हे अमितविक्रम ! हम भगवान्‌ हरिके चरणॉकी शपथ करके आपसे सच-सजच कहते हैं कि आफ्के ऐसे बल्-वीर्यकों देस्ककर हम आपको मनुष्य नहीं पान सकते
- **Translation**: 

---

