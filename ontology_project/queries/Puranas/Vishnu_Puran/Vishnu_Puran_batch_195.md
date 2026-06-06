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

### Verse 1 (Vishnu Puran 0.3881)
- **Original**: जिल्मेकीको पतित्र करनेमें समर्थ वह गड्जा जिससे उत्पन्न हुई है, यही भगवानका तीसरा परमपद है
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.3882)
- **Original**: रल-जिमलालड औः या-+--ट इति श्रीविष्णुपुराणे द्वितीयें$शे अश्टमो5्ध्यायः
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.3883)
- **Original**: 0000-00 जूहि स्‍तस नवाँ अध्याय ज्योतिश्चषक्र और शिश्ुमारक्षक्र श्रीपराझर उवाच तारामयं भगवतः शिशुमाराकृति प्रभो: । दिवि रूप॑ हरेर्यत्तु तस्य पुच्छे स्थितो ध्रुवः
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.3884)
- **Original**: 9 सैष भ्रमन्‌ भ्रामयति चन्द्रादित्यादिकान प्रहान्‌ । भ्रमन्तमनु त॑ यान्ति नक्षत्राणि च चक्रवत्‌
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.3885)
- **Original**: 2 श्रीपराशरजी बोस्छे-- आक्पतार्में भगवान्‌ विष्णुक्ता जो शिश्ुमार (गिरगिट अथया गोधा) के समान आकार- बाह्य तारामय स्वरूप देखा जाता है, उसके पुच्छ- भागमें घुल अवस्थित है
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.3886)
- **Original**: यह घुब रूवये घूमता हुआ चन्द्रमा और सूर्य आदि ग्रहोंको घुपाता है । उस भ्रमणशील घुबके साथ नक्षत्रणण भी चक्रके सपान घूमते रहते हैं
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.3887)
- **Original**: 138 श्रीविष्णुपुराण 518 _ *_£_॒_॒ [ अश्रीकिष्णुफराण >>
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.3888)
- **Original**: [आः9 सूर्याचन्द्रमसौ तारा नक्षत्राणि ग्रहै: सह। सूर्य, चन्द्रमा, तारे, नक्षत्र और अन्यान्य समस्त गरहगण वातानीकमयैब॑न्बैर्धुवे बद्धाने तानि लै
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.3889)
- **Original**: 3 वायु मकलमकी डोरीसे धुषके साथ बैंघे हुए, हैं
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.3890)
- **Original**: शिशुमाराकृति प्रोक्ते यद्॒ुप ज्योतिषां दिबि । नारायणो5यन धाझ्नां तस्याधारः स्वयं हदि
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.3891)
- **Original**: 4 उत्तानपादपुत्रस्तु तमाराध्य जगत्पतिम्‌ । स ताराशिशुमारस्य ध्रुव: पुच्छे व्यवस्थित:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.3892)
- **Original**: 5 आधार: शिशुमारस्य सर्बध्यक्षो जनार्दन: । धुवस्य झिशुमारस्तु घुवे भानुर्व्यवस्थित:
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.3893)
- **Original**: 6 तदाधारं. जगचेद॑. सदेवासुरमानुषम्‌
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.3894)
- **Original**: 7 येन विप्र विधानेन तन्मसैकमना: श्रृणु। विवस्वानष्टभिर्मासैरादायापो रसात्मिका: । वर्षत्यम्बु_ ततश्रान्नमन्नादप्यसखिलं जगत्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.3895)
- **Original**: 8 विवस्वानंशुभिस्तीक्ष्पैरादाय जगतो जलम्‌ । सोम॑ पुष्णात्यथेन्दुश्न॒ वायुनाडीमवैर्दिवि । नालैविंक्षिपते5भ्रेषु. धूमाग्न्यनिलमूर्तिषु
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.3896)
- **Original**: 9 न भ्रदयान्ति यतस्तेभ्यो जलान्यभ्राणि तान्यत: । अभ्रस्था: प्रपतन्त्थापो वायुना समुदीरिता: । संस्कार कालजनित॑ मैत्रेयासाद्य निर्मला;
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.3897)
- **Original**: 90 सरित्समुद्रभोमास्तु तथाप: प्राणिसम्भवा: । चतुष्प्रकारा भगवानादत्ते सविता मुने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.3898)
- **Original**: 11 आकाइहगड़ासलिलें तथादाय गभस्तिमान्‌ । अनभ्रगतमेबोव्याँ सद्य: क्षिपति रश्मिभि:
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.3899)
- **Original**: 12 तस्य संस्पर्शनिर्धूतपापपक्लो ट्विजोत्तम । न याति नरक॑ मत्यों दिव्यं स््रानं हि तत्स्मृतम्‌
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.3900)
- **Original**: 13 दृष्टसूय॑ हि. यद्धारि पतत्यश्रेविना दिबः। आकाशगड्ढासलिल तद्गोभि: क्षिप्यते रते:
- **Translation**: 

---

