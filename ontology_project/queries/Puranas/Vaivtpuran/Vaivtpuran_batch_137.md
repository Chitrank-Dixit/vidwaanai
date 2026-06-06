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

### Verse 1 (Vaivtpuran 8.6300)
- **Original**: कल्पमें जिस पूजनीयकी सर्वप्रथम पूजा होती उदास मनवाले हम लोगोंके सामने आये थे।
- **Translation**: 

---

### Verse 2 (Vaivtpuran 8.6301)
- **Original**: है, जिसके स्मरणमात्रसे समस्त बिप्न नष्ट हो जाते परमेश्वर! यदि भूखसे पीड़ित अतिथि गृहस्थके
- **Translation**: 

---

### Verse 3 (Vaivtpuran 8.6302)
- **Original**: हैं, तथा जो पुण्यकोी राशिस्वरूप है, मन्दिरमें घरसे अपूजित होकर चला जाता है तो क्‍या
- **Translation**: 

---

### Verse 4 (Vaivtpuran 8.6303)
- **Original**: विराजमान अपने उस पुत्रकी ओर तो दृष्टि डालो। उस गृहस्थका जीवन व्यर्थ नहीं हो जाता?
- **Translation**: 

---

### Verse 5 (Vaivtpuran 8.6304)
- **Original**: प्रत्येक कल्पमें तुम जिस सनातन ज्योति रूपका यहाँतक कि उसके पितर उसके द्वारा दिये गये ध्यान करती हो, वही तुम्हारा पुत्र है। यह पिण्डदान और तर्पणको नहीं ग्रहण करते तथा
- **Translation**: 

---

### Verse 6 (Vaivtpuran 8.6305)
- **Original**: मुक्तिदाता तथा भक्तोंके अनुग्रहका मूर्त रूप है। अग्नि उसकी दी हुई आहुति और देवगण उसके
- **Translation**: 

---

### Verse 7 (Vaivtpuran 8.6306)
- **Original**: जरा उसकी ओर तो निहारो। जो तुम्हारी द्वारा निबेदित पुष्प एवं जल नहीं स्वीकार करते।
- **Translation**: 

---

### Verse 8 (Vaivtpuran 8.6307)
- **Original**: कामनापूर्तिका बीज, तपरूपी कल्पवृक्षका फल उस अपवित्रका हव्य, पुष्प, जल और द्रव्य--सभी
- **Translation**: 

---

### Verse 9 (Vaivtpuran 8.6308)
- **Original**: और लावण्यतामें करोड़ों कामदेबोंकी निन्‍्दा मदिराके तुल्य हो जाता है। उसका शरीर मल-
- **Translation**: 

---

### Verse 10 (Vaivtpuran 8.6309)
- **Original**: करनेवाला है, अपने उस सुन्दर पुत्रकों देखों। सदृश और स्पर्श पुण्यनाशक हो जाता है।
- **Translation**: 

---

### Verse 11 (Vaivtpuran 8.6310)
- **Original**: दुर्गे! तुम क्‍यों विलाप कर रही हो? अरे, यह इसी बीच वहाँ आकाशवाणी हुई, जिसे
- **Translation**: 

---

### Verse 12 (Vaivtpuran 8.6311)
- **Original**: क्षुधातुर ब्राह्मण नहीं है, यह तो विप्रवेषमें जनार्दन
- **Translation**: 

---

### Verse 13 (Vaivtpuran 8.6312)
- **Original**: #प़ाणपतिखण्ड + 315 #ऋ#%%#&%##%#ऋ#ऋ#%ऋ#### # ###ऋ# ### ### कक $%$%%%%##%%###### ###&#######%#%% 55% हैं। अब कहाँ वह वृद्ध और कहाँ वह अतिथि? नारद! यों कहकर सरस्वती चुप हो गयीं। तब उस आकाशवाणीको सुनकर सती पार्वती भयभीत हो अपने महलमें गयीं। वहाँ * उन्होंने पलंगपर सोये हुए बालकको देखा। वह
- **Translation**: 

---

### Verse 14 (Vaivtpuran 8.6313)
- **Original**: भ्ड8 आनन्दपूर्बक मुस्कराते हुए महलकी छतके भीतरी ] न भागकों निहार रहा था। उसकी प्रभा सैकड़ों चन्द्रमाओंके तुल्य थी। वह अपने प्रकाशसमूहसे भूतलको प्रकाशित कर रहा था। हर्षपूर्वक स्वेच्छानुसार इधर-उधर देखते हुए शब्यापर उप उछल-कूद रहा था और स्तनपानकी इच्छासे रोते
- **Translation**: 

---

### Verse 15 (Vaivtpuran 8.6314)
- **Original**: समान उद्दीत्त थी। (फिर सोचने लगे--) मेरे हुए “उमा” ऐसा शब्द कर रहा था। उस अद्भुत
- **Translation**: 

---

### Verse 16 (Vaivtpuran 8.6315)
- **Original**: हृदयमें जो अत्यन्त मनोहर रूप विद्यमान था, यह रूपको देखकर सर्वमड्रला पार्वती त्रस्त हो
- **Translation**: 

---

### Verse 17 (Vaivtpuran 8.6316)
- **Original**: तो वही है। तत्पश्चात्‌ दुर्गने उस पुत्रकों शब्यापरसे शंकरजीके संनिकट गयीं और उन प्राणेश्वरसे
- **Translation**: 

---

### Verse 18 (Vaivtpuran 8.6317)
- **Original**: उठा लिया और उसे छातीसे लगाकर वे उसका मड्ल-बचन बोलीं। चुम्बन करने लगीं। उस समय वे आनन्द-सागरमें पार्वतीने कहा--प्राणपति! घर चलिये और
- **Translation**: 

---

### Verse 19 (Vaivtpuran 8.6318)
- **Original**: निमग्र होकर यों कहने लगीं--'बेटा! जैसे मन्दिरके भीतर चलकर प्रत्येक कल्पमें आप
- **Translation**: 

---

### Verse 20 (Vaivtpuran 8.6319)
- **Original**: दरिद्रका मन सहसा उत्तम धन पाकर संतुष्ट हो जिसका ध्यान करते हैं तथा जो तपस्याका
- **Translation**: 

---

