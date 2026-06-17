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

### Verse 1 (Vishnu Puran 0.10841)
- **Original**: वहाँ फेंके हुए उस बालकको एक मस्त्यने निगल लिया, किन्तु वह उसकी जठराभिसे जलकर भी न मरा
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.10842)
- **Original**: कालान्तरमें कुछ मछेरोंने उसे अन्य मछलियोंके साथ अपने जालमें फैसाया और असुस्श्रेष्ठ ञाम्बरकों निवेदन किया
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.10843)
- **Original**: उसकी नाममात्रकी पत्नी मायावती सम्पूर्ण अन्तःपुरकी स्वामिनी थी और वह सुलक्षणा सम्पूर्ण सूदों (रसोइयों) का आधिपत्य करती थी
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.10844)
- **Original**: डस मछलीका पेट चोरते ही उसमें एक अति सुन्दर बालक दिस्लायी दिया जो दग्ध हुए कामवृक्षका प्रथम अंकुर था
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.10845)
- **Original**: 'तब यह कौन है और किस प्रकार इस मछलीके पेटमें डाला गया' इस प्रकार अत्यन्त आक्षर्यचकित हुई उस सुन्दरीसे देवर्षि नारदने आकर कहा--
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.10846)
- **Original**: “हे सुन्दर भूकुटिवाली ! यह सम्पूर्ण जगतके स्थिति और संहारकर्ता भगवान्‌ बिष्णुका पुत्र है; इसे झम्बरासुरने सृतिकागृहसे चुयकर समुद्रमें फेंक दिया था । वहाँ इसे यह मत्स्य तिगल गया और अब इसीके द्वारा यह तेरे घर आ गया है। तू इस नररत्नक्त्र विश्वस्त होकर पालन कर"
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.10847)
- **Original**: खोले--नारदजीके ऐसा कहनेपर मायाबतीने उस बालककी अतिशय सुन्दरतासे मोहित हो बाल्यावस्थासे ही उसका अति अनुणगपूर्वक पालन किया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.10848)
- **Original**: हे महामते ! जिस समय वह नवयौवनके समागमसे सुझोभित हुआ तब वह गजगामिनी उसके प्रति कामनायुक्त अनुराग प्रकट करने छगी
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.10849)
- **Original**: 382 मायावती ददौ तस्मै मायास्सर्वा महामुने
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.10850)
- **Original**: प्रद्मयुप्नायानुरागान्धा प्रसजन्ती तुतां प्राह स कार्ष्णि: कमलेक्षणाम्‌ । मातृत्वमपहायाद्य किमेय वर्तसेउन्यथा
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.10851)
- **Original**: 15 सा तस्मै कथयामास न पुत्रस्त्व॑ ममेति वै । तनय॑ त्वामयं विष्णोईतवान्कालशम्बर:
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.10852)
- **Original**: 16 क्षिप्रः समुद्रे मत्स्यस्थ सम्प्राप्तों जठरान्मया । सा हि रोदिति ते माता कान्ताद्याप्यतिबत्सला
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.10853)
- **Original**: 17 श्रीपएय्शर उवाच इत्युक्तशशम्बर॑ युद्धे प्रधुज्ञ: स समाहृयत्‌ । क्रोधाकुलीकृतमना युयुथे चर महाबल:
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.10854)
- **Original**: 18 हत्या सैन्यमशेषं तु तस्य दैत्यस्य यादव: । सप्त माया व्यतिक्रम्य मायां प्रयुयुजेएष्टरमीम्‌
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.10855)
- **Original**: 19 तया जधान त॑ दैत्यं मायया कालशम्बरम्‌ । उत्पत्त्य च तया सार्द्धमाजगाम पितु: पुरम्‌
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.10856)
- **Original**: 20 अन्तःपुरे निपतितं मायावत्या समन्वितम्‌। त॑ दृष्ठा कृष्णसड्डल्पा बभूवु: कृष्णयोषित:
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.10857)
- **Original**: 29 रुक्मिणी साभवद्येम्णा सास्ऋरदृष्टिरनिन्दिता । धनन्‍्याया: खल्वयं पुत्रों वर्तते नवयौवने
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.10858)
- **Original**: 22 अस्मिन्‍्वयसि पुत्रो मे प्रद्मुप्नो यदि जीवति । सभाम्या जननी बत्स सा त्वया का विभूषिता
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.10859)
- **Original**: 23 अथवा यादृश: स्त्रेहो मम यादिग्वपुस्तव । हरेरपत्यं सुव्यक्त भवान्वत्स भविष्यति
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.10860)
- **Original**: 24 औपराशर उवाच एतसिमन्नत्तरे प्राप्तस्सह कृष्णेन नारद: । अन्तःपुरचरां देवीं रुक्मिणीं प्राह हर्षयन्‌
- **Translation**: 

---

