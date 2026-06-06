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

### Verse 1 (Vishnu Puran 0.2521)
- **Original**: ऐसा जान लेनेपर ये अनादि परमेश्वर भगवान्‌ अच्युत प्रसन्न होते हैं और उनके प्रसन्न होगेपर सभी क्रेदा क्षीण हो जाते हैं
- **Translation**: 

---

### Verse 2 (Vishnu Puran 0.2522)
- **Original**: अ्रीपराह्यरजी बोले--यह सुनकर हिरण्यकशिपुने क्रोधपूर्वक अपने राजसिंहासनसे उठकर पुत्र प्रह्मादके वक्षःस्थलमें लात मारी
- **Translation**: 

---

### Verse 3 (Vishnu Puran 0.2523)
- **Original**: और क्रोध तथा अमर्पसे जलते हुए मानो सम्पूर्ण संसारकों मार डालेगा इस प्रकार हाथ मलता हुआ बोला
- **Translation**: 

---

### Verse 4 (Vishnu Puran 0.2524)
- **Original**: हिरण्यकशिपुने कह्ा--हे विप्रचित्ते ! हे राहो ! है बल ! तुमल्लेग इसे भर्ती प्रकार नागपाशसे बाँधकर महासागरमें डाल दो, देरी मत करो
- **Translation**: 

---

### Verse 5 (Vishnu Puran 0.2525)
- **Original**: नहीं तो सम्पूर्ण लोक और दैत्य-दानव आदि भी इस मूक दुरत्माके मतक्प ही अनुगमन करेंगे [ अर्थात्‌ इसकी तरह जे भी विष्णुभक्त हो जायँंगे ]
- **Translation**: 

---

### Verse 6 (Vishnu Puran 0.2526)
- **Original**: हमने इसे बहुतेरा रोका, तथापि यह दुष्ट शात्रुकी ही स्तुति किये जाता है। ठीक है, दुशेंको तो मार देगा ही लाभदायक होता है
- **Translation**: 

---

### Verse 7 (Vishnu Puran 0.2527)
- **Original**: अश्रीपराशरजी ब्रोले--तब उन: टैत्योंते अपने स्वामीकी आज्ञाको दिशेधार्य कर लुरत्त ही उन्हें नागपाञासे बाँधकर समुद्रगें डाल दिया
- **Translation**: 

---

### Verse 8 (Vishnu Puran 0.2528)
- **Original**: 55। उस समय प्रह्मदजीके हिलने-डुलनेसे सम्पूर्ण महासागरमें हलचल मच गयी और अत्यन्त क्षोभके कारण उसमें सब ओर ऊँची-ऊँची लहरें उठने लगीं
- **Translation**: 

---

### Verse 9 (Vishnu Puran 0.2529)
- **Original**: हे महामते । उस महान्‌ जल-पूरसे सम्पूर्ण पृथिजीकों डूबती देख हिरण्यकशिपुने दैत्योंसे इस प्रकार कहा
- **Translation**: 

---

### Verse 10 (Vishnu Puran 0.2530)
- **Original**: हिरण्यकशिपु बोला--ेरे दैत्यों ! तुम इस दुर्मतिको इस समुद्रके भीतर ही किसी ओरसे खुल्म न रखकर सब ओरसे सम्पूर्ण पर्वतोंसे दबा दो
- **Translation**: 

---

### Verse 11 (Vishnu Puran 0.2531)
- **Original**: देस्बों, इसे न तो अग्रिने जलाया, न यह शज्लोंसे कटा, न सपो्से नष्ट हुआ और न वायु, विष और कृत्यासे ही क्षीण हुआ, तथा न यह मायाओंसे, ऊपरसे गिरानेसे अथवा दिग्गजोंसे ही मारा गया। यह बालक अत्यन्त दुष्ट-चित्त है, अब इसके जीवनका कोई
- **Translation**: 

---

### Verse 12 (Vishnu Puran 0.2532)
- **Original**: आ0 19 ] प्रथम अंदा 1 तदेष तोयमध्ये तु समाक्रान्तों महीधरे: । तिष्ठत्वब्दसहस्रान्तं प्राणान्हास्यति दुर्मतिः
- **Translation**: 

---

### Verse 13 (Vishnu Puran 0.2533)
- **Original**: 69 ततो दैत्या दानवाश्न पर्वतैस्त॑ महोदधों । आक्रम्य चयन चक्तुयोंजनानि सहस्नशः
- **Translation**: 

---

### Verse 14 (Vishnu Puran 0.2534)
- **Original**: 62 स चित्त: पर्वतैरन्त: सपुद्रस्थ महामतिः । तुष्टावाद्विकवेलायामेकाग्रमतिरच्युतम्‌_
- **Translation**: 

---

### Verse 15 (Vishnu Puran 0.2535)
- **Original**: 63 नमस्ते पुण्डरीकाक्ष नमस्ते पुरुषोत्तम । जपस्ते सर्वल्तोकात्मन्नमस्ते तिग्मच्रक्रिणे
- **Translation**: 

---

### Verse 16 (Vishnu Puran 0.2536)
- **Original**: 64 नमो ब्रह्मण्यदेवाय गोब्राह्मणहिताय च। जगद्िताय कृष्णाय गोब्न्दाय नमो नमः
- **Translation**: 

---

### Verse 17 (Vishnu Puran 0.2537)
- **Original**: 65 रुद्ररूपाय कल्पान्ते नमस्तुभ्य॑ त्रिमूर्तये
- **Translation**: 

---

### Verse 18 (Vishnu Puran 0.2538)
- **Original**: 66 देवा बक्षासुरा: सिद्धा नागा गन्धर्वकिन्नरा: । पिज्ञाचा राक्षसाओव मनुष्या: पशवस्तथा
- **Translation**: 

---

### Verse 19 (Vishnu Puran 0.2539)
- **Original**: 67 नकल अप सन नलिय कर स्थावराशैव +0-- । वायु: झब्दः :
- **Translation**: 

---

### Verse 20 (Vishnu Puran 0.2540)
- **Original**: 68 रूप॑ गन्धो मनो बुद्धिरात्या कालस्तथा गुणा: । एवपा परमार्थक्ष॒ सर्वमेतत्त्वमच्युत
- **Translation**: 

---

