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

### Verse 1 (Vishnu Puran 0.2841)
- **Original**: 49 निर्व्यापारमनाख्येये. व्याप्तिमात्रमनूषमम्‌ । आत्मसम्बोधविषयं सत्तामात्रमलछक्षणम्‌
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2842)
- **Original**: 50 प्रशात्तमभय्य॑ शुद्ध दुर्विभाव्यमर्सअयम्‌ । विष्णोज्ञानमयस्योक्ते तज्ज्ञानं ब्रह्मसंज्ञितम्‌
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2843)
- **Original**: 59 तत्र ज्ञाननिरोधेन योगिनो यान्ति ये लयम्‌ । संसारकर्षणोप्तौ ते यान्ति निरबीजर्ता द्विज
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2844)
- **Original**: 52 एवंप्रकारममरलं नित्य व्यापकमक्षयम्‌ । समस्तहेयरहित॑ विष्णवार्व्य॑परम॑ पदम्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2845)
- **Original**: 53 तद्ह्म परम॑ योगी यतो नावर्त्तते पुनः । अयत्यपुण्योपरमे_ क्षीणक्रेशोउतिनिर्मेल:
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2846)
- **Original**: 54 दे रूपे ब्रह्मणस्तस्थ मूत्त चामूर्तमेव च। क्षराक्षरस्वरूप ते सर्वभूतेघ्रृवस्थिते
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2847)
- **Original**: 55 अक्षर॑ तत्पर ब्रह्म क्षरं सर्बमिंदं जगत्‌। एकदेशस्थितस्यामेज्योत्त्रा विस्तारिणी यथा । एकर्देशस्थितस्यामेज्योत्स्रा परस्य ब्रह्मण: शक्तिस्तथेंद्मखिर्ले जगत्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2848)
- **Original**: 56 तन्राप्यासब्रदूरत्वाइहुत्वस्वल्पतामय: । ज्योत्म्राभेदो5स्ति तच्छक्तेस्तद्नन्पैत्रेय बिद्यते
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2849)
- **Original**: 57 ब्रह्मविष्णुशिवा ब्रह्मग्ग्रधाना ब्रह्मशक्तय:
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2850)
- **Original**: ततश्न देवा मैत्रेय नन्‍्यूना दक्षादयस्तत:
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2851)
- **Original**: 58 ततो मनुष्या: पशलों मृगपक्षिसरीसुपाः । न्यूनान्नयूनतराशैब वृक्षगुल्मादयस्तथा
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2852)
- **Original**: 59 तदेतदक्षर॑ नित्य॑ जगन्पुनिवराखिलम्‌ । जहाँसे फिर ल्लैटना नहीं पड़ता
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2853)
- **Original**: है मुने ! जो योगीकी मुक्तिका करण है, वह 'साधनालम्बन-ज्ञान' ही उस ऋष्मभूत परमपदका प्रथम भेद है"
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2854)
- **Original**: क्लैश-बन्धनसे मुक्त होनेके छिये योगाभ्यासी योगीका साध्यरूप जो ब्रह्म है, हे महामुने ! उसका ज्ञान ही 'आलम्बन-विज्ञान' नामक दूसरा भेद है।47
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2855)
- **Original**: इन दोनों साध्य-साधनोंका अभेदपूर्वक जो 'अद्टैतमय ज्ञान' है उसीको मैं तीसरा भेद कहता हूँ
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2856)
- **Original**: और हे महामुने ! उक्त तीनों प्रकारके ज्ञानकी विशेषताका निणकरण करनेपर अनुभव हुए आत्मस्वरूपके समान ज्ञानस्तरूप भगवान्‌ विष्णुका जो निर्व्यापार अनिर्वचनीय, व्याप्रिमात्र, अनुपम, आत्मबोधस्वरूप, सत्तामत्र, अलक्षण, शात्त, अभय, झुद्ध, भावषनातीत और आश्रयहीन रूप है, वह “ब्रहम' नामक ज्ञान [ उसका चौथा भेद ] है
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2857)
- **Original**: 49--51
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2858)
- **Original**: हे द्विज ! जो योगिजन अन्य ज्ञानोंका निरोधकर इस (चोथे भेद) में हो लोन हो जाते हैं वे इस संसार-क्षेत्रके भीतर जीजारोपणरूप कर्म करनेमें निर्बीज (वासनारहित) डोते हैं। [अर्थात्‌ वे लोकसंग्रहके लिये कर्म करते मी रहते हैं तो भी उन्हें उन कमांका कोई पाप-पुण्यरूप फल प्राप्त नहीं होता ]
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2859)
- **Original**: इस प्रकारका वह निर्मल, नित्य, व्यापक, अक्षय और समस्त हेय गुणोंसे रहित विष्णु नामक परमपद है
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2860)
- **Original**: पुण्य-पापका क्षय क्लेश्ोंकी निव्ति होनेपर जो अत्यन्त निर्मल हो जाता है वही योगी उस परब्रह्मका आश्रय लेता है जहाँसे बह फिर नहीं ख्ौटता
- **Translation**: 

---

