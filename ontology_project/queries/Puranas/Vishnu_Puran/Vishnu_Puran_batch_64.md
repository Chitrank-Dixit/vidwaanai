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

### Verse 1 (Vishnu Puran 0.1261)
- **Original**: '3% हिरण्यगर्भ, पुरुष, प्रधान और अव्यक्तकरूप शुद्धज्ञानस्वरूप वासुदेवकों नमस्कार है'
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.1262)
- **Original**: इस (3* नमो भगबते बासुदेवाय) मन्त्रकों पूर्वकालमें तेरे पितामह भगवान्‌ स्वायष्भुबभनुने जपा था। तब उनसे सन्तुष्ट होकर श्रोजनार्दनने उन्हें त्रिल्पेकीमें दुर्लभ मनोवाज्छित सिद्धि दी थीं। उसी प्रकार तू भी इसका निरन्तर जप करता हुआ श्रोगोविन्दको प्रसन्न कर
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.1263)
- **Original**: 56-517
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.1264)
- **Original**: आज औ प इति श्रीविष्णुपुराणे प्रथमेंडशे एकादशोउध्यायः
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.1265)
- **Original**: अर 12 ] प्रथम अंध् बारहवाँ अध्याय धुबकी तपस्यासे प्रसन्न हुए भगवानका आविर्भाब और उसे घुबपद-दान ऑपराजर उवाच निशम्यैतदशेषेण मैत्रेय नृपतेः सुतः
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.1266)
- **Original**: निर्जगाम वनात्तस्मात्मणिपत्य स तानृषीन्‌
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.1267)
- **Original**: 1 कृतकृत्यमिवात्मानं मन्‍्यमानस्ततो छ्विंज । म्रधुसंज्ञ महापुण्ये जगाम यमुनातटम्‌
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.1268)
- **Original**: 2 पुनश्च मधुसंज्ञेन दैत्येनाधिष्ठित॑ यतः । ततो मधुवन नाप्ना ख्यातमत्र महीतले
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.1269)
- **Original**: 3 हत्वा च लवण रक्षो मधुपुत्रं महाबलम्‌। जजन्नुप्नो मधुरां नाम पुरी यत्र चकार वै
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.1270)
- **Original**: । 4 यत्र वे देवदेवस्थ सान्निध्यं हरिमेधसः । सर्वपापहरे तस्मिस्तपस्तीर्थे चकार सः
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.1271)
- **Original**: 5 मरीचिमुख्यैर्मुनिभिर्यथोद्दिष्टमभूत्तथा.
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.1272)
- **Original**: आत्मन्यशेषदेवेशं स्थितं विष्णुमपन्यत
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.1273)
- **Original**: 6 अनन्यचेतसस्तस्य ध्यायतो भगवान्हरि: । सर्वभूतगतो विप्र सर्वभावगतो&भवत्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.1274)
- **Original**: 7 मनस्यवस्थिते तस्मिन्विष्णौ मैश्रेय योगिन: । न झश्ाक धरा भारस॒द्रोदू भूतधारिणी
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.1275)
- **Original**: 8 वामपादस्थिते तस्मिन्नामाद्ेंन मेदिनी । द्वितीयं च ननामाद्ध॑ क्षिते्दक्षिणत: स्थिते
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.1276)
- **Original**: 9 पादाडुष्टेन सम्पीक्षय यदा स वसुधां स्थित: । तदा समस्ता वसुधा चाल सह पर्वत:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.1277)
- **Original**: 10 नहो नदाः समुद्राश्ष सक्लेभ॑ परम ययुः । तत्क्षोभादमरा: क्षोभ॑ पर॑ं जम्मुर्महामुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.1278)
- **Original**: 19 यामा नाम तदा देवा मैत्रेथ परमाकुला: । इुन्द्रेण सह सम्मन्त्रय ध्यानभज़ूँ प्रचक्रमु:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.1279)
- **Original**: 12 कूष्माण्डा विविधै रूपेमहिन्रेण महामुने । समाधिभडुमत्यन्तमारव्धा: कर्त्तुमातुरा:
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.1280)
- **Original**: 13 सुनीतिरनाम तन्माता सास््रा तत्युरतः स्थिता । पुत्रेति करुणां बाचमाह मायामयी तदा
- **Translation**: 

---

