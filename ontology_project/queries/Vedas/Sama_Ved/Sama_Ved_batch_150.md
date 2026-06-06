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

### Verse 1 (Sama Ved 0.2981)
- **Original**: है पवित्र होने वाले तेजोमय सोमदेव ! दिन के तीनों सवनों में प्रयुक्त जो अन्न, प्रशंसित, बलवर्द्धक, मधुर तथा उत्तम पुत्र प्रदान करने वाला है, हमारे उस्त पोषक अन्न को आप अपनी तरंगों से शुद्ध करें
- **Translation**: 

---

### Verse 2 (Sama Ved 0.2982)
- **Original**: 1155. न किष्टं कर्मणा नशद्यश्नकार सदावृधम्‌ । इन्द्रं न यज्ञैविश्वगूर्तमृ भ्वसमधृष्टं धृष्मुमोजसा
- **Translation**: 

---

### Verse 3 (Sama Ved 0.2983)
- **Original**: वृद्धिदायक, सभी के स्तुत्य, महान्‌, तेजस्वी, अपराजेय, शत्रुओं को पराभूत करने वाले इन्द्रदेव का, जो बजमान यज्ञ द्वारा यजन (सत्कार) करते हैं, उन्हें अपने प्रभाव-पुरुषार्थ (कर्म) से कोई नष्ट नहीं कर सकता
- **Translation**: 

---

### Verse 4 (Sama Ved 0.2984)
- **Original**: 1156. अषाढमुग्रं पृतनासु सासहिं यस्मिन्महीरुरुज़य: । सं धेनवो जायमाने अनोनवुर्द्याव: क्षामीरनोनवु:
- **Translation**: 

---

### Verse 5 (Sama Ved 0.2985)
- **Original**: जिन इन्द्रदेव के प्राकट्य पर (उनके महान्‌ प्रभाव से) महान्‌ वेगवाली (पशु) गौएँ उन्हें प्रणाम करती हैं, और पृथ्वी तथा आकाश भी उनके समक्ष झुककर अभिवादन करते हैं, उन उग्र, शत्रु विजेता और पराक्रमी इन्द्रदेव की हम स्तुति करते हैं
- **Translation**: 

---

### Verse 6 (Sama Ved 0.2986)
- **Original**: इति चतुर्थ: खण्ड:
- **Translation**: 

---

### Verse 7 (Sama Ved 0.2987)
- **Original**: के के के
- **Translation**: 

---

### Verse 8 (Sama Ved 0.2988)
- **Original**: पञ्षम: खण्ड:
- **Translation**: 

---

### Verse 9 (Sama Ved 0.2989)
- **Original**: । 1157, सखाय आ नि षीदत पुनानाय प्रगायत । शिशुं न यज्ञैः परि भूषत थ्रिये
- **Translation**: 

---

### Verse 10 (Sama Ved 0.2990)
- **Original**: 9 हे भित्रो ! बैठकर पवित्र होने वाले सोम के लिए स्तुतिगान करो । पिता द्वारा पूत्र को अलंकृत करने के समान सोम को हवि आदि पदार्थों द्वारा यज्ञ में विभुषित करो
- **Translation**: 

---

### Verse 11 (Sama Ved 0.2991)
- **Original**: 8.6 सामवेद- संहिता 1158. समी वत्सं न मातृभि: सृजता गयसाधनम्‌ ।देवाव्यं3मदमभि द्विशवसम्‌ ।।2!
- **Translation**: 

---

### Verse 12 (Sama Ved 0.2992)
- **Original**: हे ऋत्विग्गण ! घर के साधनभूत, दिव्य गुणों के रक्षक, आनन्दवर्द्धक, दोनों प्रकार (दिव्य और पार्थिव) से बलवर्द्धक इस सोम को उसी प्रकार जल से मिश्रित करें, जैसे माताओं के साथ बच्चे मिलकर रहते हैं
- **Translation**: 

---

### Verse 13 (Sama Ved 0.2993)
- **Original**: 1159, पुनाता दक्षसाधनं यथा शर्धाय वीतये ।यथा मित्राय वरुणाय शन्तमम्‌
- **Translation**: 

---

### Verse 14 (Sama Ved 0.2994)
- **Original**: (हे त्रग्रत्वजो !) गतिशीलता प्राप्त करने के लिए, देवों (दिव्यज्ञान) को प्रदान करने के लिए, अधिकाधिक सुखप्रद बनाने के लिए, बल वृद्धि के लिए तथा मित्र और वरुण देवों के लिए सोम का शोधन करें
- **Translation**: 

---

### Verse 15 (Sama Ved 0.2995)
- **Original**: 3 । 1160. प्र वाज्यक्षा: सहस्नधारस्तिर: पवित्र वि वारमव्यम्‌
- **Translation**: 

---

### Verse 16 (Sama Ved 0.2996)
- **Original**: बलयुकक्‍त और अनेक धाराओं से छाना जाने वाला सोम, ऊन के शोधक छन्‍्ने से छतकर टपकता है
- **Translation**: 

---

### Verse 17 (Sama Ved 0.2997)
- **Original**: 11691. स वाज्यक्षा: सहस्नरेता अद्धिर्मजानों गोभि: श्रीणान:
- **Translation**: 

---

### Verse 18 (Sama Ved 0.2998)
- **Original**: असंख्य बलों से युक्त, जल से शोधित किया हुआ, गो-दुग्ध आदि से मिश्रित वह बलशाली सोम छनता हुआ (पात्र में) जाता है
- **Translation**: 

---

### Verse 19 (Sama Ved 0.2999)
- **Original**: 1162. प्र सोम याहीदद्धस्य कुक्षा नृभियेमानो अद्विभि: सुतः
- **Translation**: 

---

### Verse 20 (Sama Ved 0.3000)
- **Original**: पाषाणों से कूटकर निष्पादित हुआ, त्रग्रत्विजों द्वारा विधिपूर्वक पवित्र किया हुआ सोमरस, इन्द्रदेव के उदर (रूप कलश) में प्रविष्ट हो
- **Translation**: 

---

