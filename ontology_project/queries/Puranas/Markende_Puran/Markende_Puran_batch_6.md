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

### Verse 1 (Markende Puran 0.101)
- **Original**: अभाव तथा अभावके बाद भाव, इस प्रकार। उनका विब्धन 715ओ+-- उं+5+ खि>+ताण-न न सस...3.32ल्‍लअन्‍स«न»+ ..स्‍ममन्‍ंममस्‍न्‍त0ता.. अं. लनम«म>«%»न-.. रन» न... ल्‍अअअसर«7गन्‍«-+-
- **Translation**: 

---

### Verse 2 (Markende Puran 0.102)
- **Original**: * थर्मपश्लीद्वात जेमिनिके प्रश्नॉक्ता उत्तर *« श्श 66484 4.2.2:5<
- **Translation**: 

---

### Verse 3 (Markende Puran 0.103)
- **Original**: 90*-%6:2.2:7 + &4:4.0# *24068.2:0-7+ +65:2:07774:62.2+0+ 44000 + [3200 0%4 2.07 0 46000 66.24 7
- **Translation**: 

---

### Verse 4 (Markende Puran 0.104)
- **Original**: प्रिवा द्रौपदोके पाँच महारधी पुड, जितका अभी क्किहतक कहीं दुआ था. समस्त फाण्डव जिनके रक्षक थे तथा जो स्तर्थ भी थह्े अलयान्‌ थे, अनाथक्रों भाँति कैसे मारे गये? महाभारतके विष4में यह मेरा सन्देष्ठ हैं। आफलोग इसका निश्ारण करें। चक्षियोंने कहा--जो क्षम्पू्ण देखताओंके स्थामों, सर्वव्यापक, सकको ठत्पत्तिक कारण, अन्तर्यामी, प्रमाणोंके अतिपत्न, सनातन, अविनाशों, यतृर्ब्युह- स्थरूप, शिगुणमण, निर्शुण, सन्नसे बडे, अत्यन्त
- **Translation**: 

---

### Verse 5 (Markende Puran 0.105)
- **Original**: गौरबश्ाली, सर्वश्नेठ्ठ तथा अमृतस्वस्प हैं, ठन 4 भगलान्‌ ठिष्णुझो हम सबसे पहले नमस्कार करते है। जिनसे जडकर सूक्ष्म तथा जिनसे अधिक घड़ा भो कोर नहों है, जिनके द्वारा यह राम्पूर्ण लिन * 05 न्‍7>-0
- **Translation**: 

---

### Verse 6 (Markende Puran 0.106)
- **Original**: व्यू) है, जो इस जगवके आदिकारण और प्रक्षियोँने कहा--गब्रह्मन! आपका प्रश्न यदि
- **Translation**: 

---

### Verse 7 (Markende Puran 0.107)
- **Original**: अयान्सा हैं, जो उत्पात, लग, प्रत्यक्ष और हमारी छुल्िके ग्राह"ट गे होगा तो हम अवश्य
- **Translation**: 

---

### Verse 8 (Markende Puran 0.108)
- **Original**: परोक्ष--सश्रसे ल्रिलक्षण हैं, इस सम्पूर्ण जातृको उस्स्य समाधात करेंगे। आप निःशडू होकर सु्नें।
- **Translation**: 

---

### Verse 9 (Markende Puran 0.109)
- **Original**: जिएको रचता बतलति हैं तथा अनतमें जिनके विप्वर ! यादें वेद, धर्मशास्त्र, सम्पूर्ण बेदाद्न तथा
- **Translation**: 

---

### Verse 10 (Markende Puran 0.110)
- **Original**: भीतर इसका संहार होगा है, तन परेश्वरकों जो चेदोंके समान साननीय इतिहास-
- **Translation**: 

---

### Verse 11 (Markende Puran 0.111)
- **Original**: हमारा गमस्कार है। तत्पशात्‌ जो अपने छारों पुशाणादि हैं, उत संबपें हमारों शुद्धिका प्रवेश है;
- **Translation**: 

---

### Verse 12 (Markende Puran 0.112)
- **Original**: मु्ोंसे ऋक्‌-साम आदि बटॉफा उच्चारण करते रुथायि हप कोई प्रतिज्ञा नहीं कर सकते। आपको
- **Translation**: 

---

### Verse 13 (Markende Puran 0.113)
- **Original**: हुए होनों लोकॉको पवित्र रूरते हैं, उन आदिदेव महाभारतमें जो-जो सच्धिध बात जान पड़े, उसे
- **Translation**: 

---

### Verse 14 (Markende Puran 0.114)
- **Original**: ब्रद्माजीकों भी हम एकआय्ितरसे नमस्कार करते निर्भीक होकर पूछिये। हैं। इसी प्रकार जिलके एक ही ब्राणसे पराजित्त जैमिनि बोले--पश्चियो ! आपलेगेका अन्त:-
- **Translation**: 

---

### Verse 15 (Markende Puran 0.115)
- **Original**: होकर असुरगण कभो याक्षिकोंके यज्ञॉका विताश ऊर्ण निर्मल है! मसहाभारतमें मेरे लिये जो
- **Translation**: 

---

### Verse 16 (Markende Puran 0.116)
- **Original**: नहीं करते, उन भगवान्‌ शह्गरकों भी मस्तक सॉन्‍्टिग्ध बातें हैं, उन्हें बताता हूँ; रुतियें और
- **Translation**: 

---

### Verse 17 (Markende Puran 0.117)
- **Original**: झ्ुकाते हैं। उसके बाद हन अद्भुत ऋरम करनेठाले सुनकर उनकी व्वाख्वा कोजिये। सर्वव्यापी भगवा-[
- **Translation**: 

---

### Verse 18 (Markende Puran 0.118)
- **Original**: व्यसजीके सम्पूर्ण नतोंकों ण्याख्ता करेंगे, जिन्होंने जनार्दन सम्पूर्ण जगत्‌के आधार, समस्त कारणोंके
- **Translation**: 

---

### Verse 19 (Markende Puran 0.119)
- **Original**: भहाभास्तके उद्देश्यस्े धर्म आदिका रहस्य प्रकट भी कारण और निर्गुण होते हुए भी मनुष्य-
- **Translation**: 

---

### Verse 20 (Markende Puran 0.120)
- **Original**: किया है। तत्तदर्शी मुनियोंने जलका ' नाए।' कहा शरोस्को कस प्राप्त हुए? द्पदकुमारों कृष्णा! है। वह +ग हो पर्दकालमें भगवानूका निवासस्थान अकेलों हों पाँच पाण्टवॉको महारानी क्योंक
- **Translation**: 

---

